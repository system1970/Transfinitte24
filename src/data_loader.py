import requests
from bs4 import BeautifulSoup
from io import BytesIO
import PyPDF2

def scrape_competitor_data(url: str):
    
    response = requests.get(url)
    response.raise_for_status() 
    
    print(response)
    
    if url.split(".")[-1]=="pdf":
        pdf_file = BytesIO(response.content)

        # Step 3: Read the PDF using PyPDF2
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        
        # Step 4: Loop through the pages and extract text
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        
        # Step 5: Output the extracted text
        print(text)
        print(len(text))
        return (text) if text else "No content found"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print(soup)

    print("Scraping Over.")
    print(len(soup.get_text(strip=True)))
    return soup.get_text(strip=True) if soup else "No content found"
