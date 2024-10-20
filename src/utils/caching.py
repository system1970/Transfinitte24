import sqlite3
import hashlib 
from pydantic_models import CompetitiveIntelligence
from typing import Optional


def cache_insights(cursor, conn, text: str, insights: CompetitiveIntelligence):
    text_hash = hashlib.sha256(text.encode()).hexdigest()  # Create a hash of the input text
    cursor.execute("INSERT OR REPLACE INTO insights_cache (text_hash, insights) VALUES (?, ?)", 
                   (text_hash, insights.json()))
    conn.commit()

# Function to retrieve cached insights from SQLite
def retrieve_cached_insights(cursor, conn, text: str) -> Optional[CompetitiveIntelligence]:
    text_hash = hashlib.sha256(text.encode()).hexdigest()
    cursor.execute("SELECT insights FROM insights_cache WHERE text_hash = ?", (text_hash,))
    row = cursor.fetchone()
    if row:
        return CompetitiveIntelligence.parse_raw(row[0])
    return None