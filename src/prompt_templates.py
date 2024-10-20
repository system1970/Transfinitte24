# prompt_templates.py

# Business Model Insights Template
business_model_prompt_template = """
You are given the following text from a business report:
{document}
Extract key insights for the following areas:
- Channels (store, online, B2B)
- Product portfolio (categories, assortment size, private labels)
- Customer segments served
- Marketing strategy and media presence
- Affordability offerings (financing, exchange, etc.)
- After-sales offerings (customer service, recycling/disposal)
- Supply chain (network, delivery promises)
- Use of technology

Return the information as a JSON object.
"""

# Geographical Presence Insights Template
geographical_presence_prompt_template = """
You are given the following text from a business report:
{document}
Extract key insights for the geographical presence of the company, including:
- Number of stores by location
- New store additions in the last year
- Future store plans
- Store types (rented or owned)
- Store formats (size, type, manpower)
- Space used for advertising

Return the information as a JSON object.
"""

# Performance Trends Insights Template
performance_trends_prompt_template = """
You are given the following text from a business report:
{document}
Extract key performance trends for the company, including:
- Financial performance over time
- Store unit economics (capital expenditure, working capital, sales per square foot)
- Break-even analysis
- Performance by region and product category

Return the information as a JSON object of the below format

'Financial Performance': Financials

"""

# Strategic Initiatives Insights Template
strategic_initiatives_prompt_template = """
You are given the following text from a business report:
{document}
Extract key strategic initiatives for the company, including:
- Investments
- Acquisitions
- Other major strategic initiatives

Return the information as a JSON object in the below format

"Investments": 
    "amount": amount,
    "area": area,
"Acquisitions": 
    "company": company,
    "state": stake,
"Other Initiatives": 
    "initiative": initiative
    
"""

# Future Outlook Insights Template
future_outlook_prompt_template = """
You are given the following text from a business report:
{document}
Extract key insights for the company's future outlook, including:
- Planned future investments or expansions
- Anticipated market trends
- Expected performance in the coming years
- Growth opportunities

Return the information as a JSON object.
"""
