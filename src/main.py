import time
from competitor_scraper import get_competitor_urls
from data_loader import scrape_competitor_data
from langchain_extraction import extract_insights
from ai_analysis import analyze_insights
from dotenv import load_dotenv
import sqlite3,hashlib

from pydantic_models import CompetitiveIntelligence

load_dotenv()

def get_db_connection():
    # Create a new connection to the SQLite database
    conn = sqlite3.connect('./Caching/cache.db')
    return conn

# Function to generate cache key (for URLs)
def generate_url_key(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()

# Function to check if the URL data is cached
def get_cached_data(conn, cursor, url: str) -> str:
    cursor.execute('SELECT response FROM url_cache WHERE url = ?', (url,))
    result = cursor.fetchone()
    return result[0] if result else None

# Function to store the scraped data in cache
def cache_data(conn, cursor, url: str, response: str):
    cursor.execute('REPLACE INTO url_cache (url, response) VALUES (?, ?)', (url, response))
    conn.commit()

def get_analysis(competitor_name = None):
    # # Get the competitor's name from user input
    if not competitor_name:
        competitor_name = input("Enter the name of the competitor: ")
    # Get URLs of competitors to scrape data from
    try:
        competitor_urls = get_competitor_urls(competitor_name)
    except:
        pass
    
    analysis = None 
    
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create table for caching URL data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS url_cache (
            url TEXT PRIMARY KEY,
            response TEXT
        )
    ''')
    conn.commit()
    
    # Iterate over each competitor's URL and extract insights
    for url in competitor_urls:
        print(f"Processing URL: {url}")
        # Check if the URL's data is cached
        cached_data = get_cached_data(conn, cursor, url)
        
        if cached_data:
            print(f"Using cached data for URL: {url}")
            text = cached_data
        else:
            print(f"Scraping data from: {url}")
            text = None
            retries = 4
            while not text and retries > 0:
                try:
                    text = scrape_competitor_data(url)  # Scrape competitor data
                    # Cache the scraped data
                    cache_data(conn, cursor, url, text)
                except Exception as e:
                    print(e, "Scraping Error")
                    time.sleep(15)
                    retries -= 1

        # If scraping failed and no data was retrieved
        if not text:
            print(f"Failed to retrieve data from {url} after multiple attempts.")
            continue
        try:
            insights = extract_insights(text[:15000])  # Extract competitive intelligence
            analysis = analyze_insights(insights)  # Analyze the extracted insights
             # Print or store the analysis result
            print("Analysis Result:")
            for key, value in analysis.items():
                print(f"{key}: {value}")
            break
        except Exception as e:
            print(e)
            analysis = analyze_insights(CompetitiveIntelligence())

    return analysis

if __name__ == "__main__":
    get_analysis()
