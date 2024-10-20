📊 Competitor Insights & Data Visualization Project
This project provides a streamlined solution for extracting, analyzing, and visualizing competitor data. It uses LangChain to scrape competitor insights, transforms them into a structured format, and visualizes the results using Streamlit and streamlit-echarts for interactive charting.

🚀 Features
Data Scraping & Extraction: Automatically scrapes competitor data using LangChain and stores it in a structured format (JSON).
Intelligent Analysis: Extracts meaningful insights from scraped data (e.g., competitor performance trends, store presence, marketing strategies).
Interactive Data Visualization: Displays graphs and visualizations of competitor insights directly in a web app using Streamlit and Echarts.
Caching with SQLite: Ensures URLs are cached along with their outputs, avoiding redundant scraping and speeding up repeated requests.
🛠️ Installation
Clone the repository:
bash
Copy code
git clone https://github.com/system1970/Transfinitte24.git
cd competitor-insights
Create a virtual environment (optional but recommended):
bash
Copy code
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Dependencies:

streamlit: For building the web app.
streamlit-echarts: For interactive graph visualizations.
langchain: For scraping competitor insights and performing NLP tasks.
sqlite3: For caching scraped results.
pydantic: For data validation and modeling.
Set up environment variables:

Create a .env file in the root directory and add your environment variables. For example:

plaintext
Copy code
OPENAI_API_KEY=your_openai_key_here
📂 Project Structure
bash
Copy code
.
├── backend.py                 # Backend logic for scraping and data extraction
├── data_loader.py             # Helper functions for scraping competitor data
├── competitor_scraper.py       # Scraping competitor URLs
├── langchain_extraction.py     # LangChain-based insight extraction
├── ai_analysis.py             # Analyzes extracted insights
├── pydantic_models.py         # Pydantic models for data validation
├── streamlit_app.py           # Main Streamlit app with data visualization
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables (ignored in version control)
└── README.md                  # Project documentation (this file)
💻 Running the Application
1. Running the Backend Analysis
You can test the backend scraping, analysis, and insights extraction using:

bash
Copy code
python backend.py
This will prompt you to input a competitor name and then run the analysis, scraping competitor data, and extracting insights.

2. Running the Streamlit Web App
To run the web interface for visualizing competitor insights:

bash
Copy code
streamlit run streamlit_app.py
Then, open your browser and go to the local URL provided (e.g., http://localhost:8501). Upload your JSON data or scrape it using the backend and visualize it in real time!

🗄️ Caching Mechanism
The project uses SQLite to cache competitor URLs and their scraped data, preventing repeated requests and improving the efficiency of subsequent analyses. If a URL has been scraped before, the data is fetched from the cache instead of performing a new scrape.

📊 Visualizing Data
The visualizations are powered by streamlit-echarts. Once the data is extracted, various insights such as store locations, marketing strategies, financial performance, etc., are visualized as interactive graphs.

Example chart visualized:


Changing Chart Types
By default, the charts are line graphs. However, you can change the graph type by modifying the type in the series option inside the streamlit_app.py file:

python
Copy code
series = [
    {
        "data": y_data,
        "type": "bar"  # Change this to "line", "scatter", etc.
    }
]
🤖 LangChain for Insights Extraction
LangChain is used to process and extract competitive insights from raw scraped data, offering a highly flexible and powerful natural language processing (NLP) tool for automatic data structuring.

Example of Insights Extraction:
json
Copy code
{
  "Channels": {
    "Store": "7100 retail sales outlets across India",
    "Online": "No information available",
    "B2B": "1000 direct sales agents"
  },
  "Product Portfolio": {
    "Categories": "Textiles, Plastics, Petrochemicals"
  },
  ...
}
These insights are then transformed into graphable data for further analysis.

🧑‍💻 Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request with your improvements.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.