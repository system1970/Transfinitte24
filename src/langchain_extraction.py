import json
from langchain.chains import LLMChain
from langchain_groq import ChatGroq # type: ignore
from langchain.prompts import PromptTemplate
from pydantic_models import CompetitiveIntelligence, StrategicInitiatives, BusinessModel, GeographicalPresence, PerformanceTrends
from prompt_templates import (
    business_model_prompt_template,
    geographical_presence_prompt_template,
    performance_trends_prompt_template,
    strategic_initiatives_prompt_template,
    future_outlook_prompt_template,
)
from dotenv import load_dotenv
from utils.caching import retrieve_cached_insights, cache_insights
import sqlite3

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0
)

json_fix_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
        The following text contains a potentially malformed JSON structure:
        {text}
        Your task is to correct the JSON format and return a valid JSON object.
        Make sure to fix any missing or incorrect quotes, commas, and braces.
        Ensure it can be parsed by a standard JSON parser. Don't output anything else other than the JSON object.
    """
)

def parse_json_or_none(output: str):
    """Helper function to parse JSON output from LLM, returns None if parsing fails."""
    chain = LLMChain(llm=llm, prompt=json_fix_prompt)
    
    # Get the corrected JSON string from the model
    corrected_json_str = chain.run(output).replace("```", "").replace("json", "")
    
    # Attempt to parse the corrected JSON string
    
    max_retries = 5
    while max_retries > 0:
        try:
            corrected_json = json.loads(corrected_json_str)
            return corrected_json
        except json.JSONDecodeError as e:
            print(corrected_json_str)
            print(e)
            corrected_json_str = chain.run(corrected_json_str+f"\n{e}I repeat this is very important Don't output anything else other than the JSON object.")
            max_retries-=1
    return None

def get_db_connection():
    # Create a new connection to the SQLite database
    conn = sqlite3.connect('./Caching/cache.db')
    return conn
    
def extract_insights(text: str) -> CompetitiveIntelligence:
    """Extract insights using LangChain-Groq LLaMA API."""
    
    conn = get_db_connection()  # Get a new connection
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS insights_cache (
        text_hash TEXT PRIMARY KEY,
        insights TEXT
    )
    ''')
    conn.commit()
    
    cached_insights = retrieve_cached_insights(cursor, conn, text)
    if cached_insights:
        print("Returning cached data...")
        return cached_insights 

    # 1. Extract Business Model Insights
    business_model_chain = LLMChain(llm=llm, prompt=PromptTemplate(
        input_variables=["document"],
        template=business_model_prompt_template
    ))
    business_model_result = business_model_chain.run(text)
    business_model_data = parse_json_or_none(business_model_result)
    business_model_data = {"_".join(key.lower().split()): value for key,value in business_model_data.items()}
    business_model_data = {"_".join(key.lower().split()): value for key, value in business_model_data.items()}
    print("Business model Data Gathered.", business_model_data)
    
    # 2. Extract Geographical Presence Insights
    geographical_chain = LLMChain(llm=llm, prompt=PromptTemplate(
        input_variables=["document"],
        template=geographical_presence_prompt_template
    ))
    geographical_result = geographical_chain.run(text)
    geographical_data = parse_json_or_none(geographical_result)
    geographical_data = {"_".join(key.lower().split()): value for key,value in geographical_data.items()}
    geographical_data = {"_".join(key.lower().split()): str(value) for key, value in geographical_data["geographical_presence"].items()}
    print("geographical_data Data Gathered.", geographical_data)
    
    # 3. Extract Performance Trends Insights
    performance_chain = LLMChain(llm=llm, prompt=PromptTemplate(
        input_variables=["document"],
        template=performance_trends_prompt_template
    ))
    performance_result = performance_chain.run(text)
    performance_data = parse_json_or_none(performance_result)
    print("performance_data gathered", performance_data)
    performance_data = {"_".join(key.lower().split()): value for key,value in performance_data.items()}
    performance_data = {"_".join(key.lower().split()): value for key, value in performance_data["financial_performance"].items()}
    
    # 4. Extract Strategic Initiatives Insights
    strategic_chain = LLMChain(llm=llm, prompt=PromptTemplate(
        input_variables=["document"],
        template=strategic_initiatives_prompt_template
    ))
    strategic_result = strategic_chain.run(text)
    strategic_data = parse_json_or_none(strategic_result)
    print("strategic_data gathered", strategic_data)
    strategic_data = {"_".join(key.lower().split()): value for key,value in strategic_data.items()}
    # if "in"
    # if type(strategic_data["investments"])==list:
    #     if len(strategic_data["investments"]):
    #         strategic_data = {"_".join(key.lower().split()): value for key, value in strategic_data["investments"][0].items()}
    # elif type(strategic_data["investments"])==dict:
    #     strategic_data = {"_".join(key.lower().split()): value for key, value in strategic_data["investments"].items()}
    
    # 5. Extract Future Outlook Insights
    future_chain = LLMChain(llm=llm, prompt=PromptTemplate(
        input_variables=["document"],
        template=future_outlook_prompt_template
    ))
    future_outlook_result = future_chain.run(text)
    future_outlook_data = parse_json_or_none(future_outlook_result)
    
    # Combine all extracted results into CompetitiveIntelligence model
    insights =  CompetitiveIntelligence(
        business_model=BusinessModel(**business_model_data) if business_model_data else None,
        geographical_presence=GeographicalPresence(**geographical_data) if geographical_data else None,
        performance_trends=PerformanceTrends(**performance_data) if performance_data else None,
        strategic_initiatives=StrategicInitiatives(**strategic_data) if strategic_data else StrategicInitiatives(),
        future_outlook= (future_outlook_data) if future_outlook_data else {}
    )
    cache_insights(cursor, conn, text, insights)
    conn.close()
    return insights
