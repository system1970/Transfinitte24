import json
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

# Initialize LLM model
llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)

# Define a prompt template to extract data points for graphing
graph_data_prompt = PromptTemplate(
    input_variables=["json_data"],
    template="""
    The following is a JSON object:
    {json_data}

    Your task is to extract key numeric data points from this JSON object. 
    Return them as a list of key-value pairs that are graphable (x, y or labels, values).
    Ensure the output is suitable for line charts, bar charts, or scatter plots.

    Return the result in a JSON format with keys like:
    - x_data (labels or categories)
    - y_data (numeric values)
    It should only be Json DONT GIVE ME CODE
    """
)

# Function to extract graphable data using LangChain and LLM
def extract_graph_data(json_data: dict):
    # Convert JSON data to string for the prompt
    json_data_str = json.dumps(json_data)

    # Create a LangChain instance with the graph data prompt
    graph_chain = LLMChain(llm=llm, prompt=graph_data_prompt)

    # Run the chain to get graphable data
    graph_data_output = graph_chain.run(json_data=json_data_str)

    # Parse the result into a usable dictionary
    try:
        print(graph_data_output)
        graph_data = json.loads(graph_data_output)
        return graph_data
    except json.JSONDecodeError as e:
        print(f"Error decoding graph data: {e}")
        return None

# Backend function that will be called by the Streamlit app
def get_graph_data_for_streamlit(json_data):
    return extract_graph_data(json_data)
