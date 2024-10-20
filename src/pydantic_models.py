from pydantic import BaseModel, conlist
from typing import List, Optional, Dict, Any

class BusinessModel(BaseModel):
    channels: Optional[str | Dict[str, Any]] = None  # e.g., {'Store': '7100 retail sales outlets across India'}
    product_portfolio: Optional[str | Dict[str, Any]] = None  # e.g., {'Categories': 'Polyester textile', 'Assortment Size': 'N/A'}
    customer_segments: Optional[str | Dict[str, Any]] = None  # e.g., {'Geographic': 'Rural and urban areas', 'Demographic': 'N/A'}
    marketing_strategy: Optional[str | Dict[str, Any]] = None # e.g., {'Pricing Strategy': 'Innovative pricing', 'Advertising': 'N/A'}
    affordability_offerings: Optional[str | Dict[str, Any]] = None # e.g., {'Financing': 'N/A', 'Exchange': 'N/A'}
    after_sales_offerings: Optional[str | Dict[str, Any]] = None # e.g., {'Customer Service': '4800 customer care executives', 'Recycling': 'N/A'}
    supply_chain: Optional[str | Dict[str, Any]] = None # e.g., {'Network': 'Reliance Logistics', 'Delivery': 'N/A'}
    use_of_technology: Optional[str | Dict[str, Any]] = None # e.g., {'Modern Technologies': 'Used at retail outlets', 'Other': 'N/A'}
    
class GeographicalPresence(BaseModel):
    number_of_stores: Optional[int | str] = None # e.g.,
    store_location: Optional[str] = None # e.g.,
    new_store_additions: Optional[str] = None
    future_store_plans: Optional[str] = None
    stores_rented_vs_owned: Optional[str] = None # e.g., '70% owned, 30% rented'
    store_formats: Optional[Dict[str, Any] | Any] = None # e.g., {'Size': 'Large', 'Type': 'Supermarket', 'Manpower': 'N/A'}
    space_used_for_advertising: Optional[str] = None
    international_presence: Optional[str] = None
    rural_presence: Optional[str] = None

class PerformanceTrends(BaseModel):
    financials: Optional[Dict[str, Any]] = None # e.g., {'Net Profit': 'Rs. 1000 crore', 'Sales': 'N/A'}
    store_unit_economics: Optional[Dict[str, Any]] = None # e.g., {'CapEx': 'N/A', 'Sales per Square Foot': 'N/A'}
    customer_feedback: Optional[Dict[str, Any]] = None # e.g., {'NPS': 'N/A', 'Reviews': 'N/A'}

class StrategicInitiatives(BaseModel):
    investments: Optional[List[Dict[str, Any]] | Dict[str, Any] ] = None # e.g., [{'Year': 2001, 'Description': 'Investment desc'}]
    acquisitions: Optional[List[Dict[str, Any]] | Dict[str, Any]] = None # e.g., [{'Year': 2007, 'Description': 'Acquisition desc'}]
    other_initiatives: Optional[List[Dict[str, Any]] | Dict[str, Any]] = None # e.g., [{'Year': 1982, 'Description': 'Initiative desc'}]

class CompetitiveIntelligence(BaseModel):
    business_model: Optional[BusinessModel] = None
    geographical_presence: Optional[GeographicalPresence] = None
    performance_trends: Optional[PerformanceTrends] = None
    strategic_initiatives: Optional[StrategicInitiatives] = None
    future_outlook: Optional[Dict] = None  # This could be a description or any content type

# business_data = {'Channels': {'Store': '7100 retail sales outlets across India', 'Online': 'No information available', 'B2B': '1000 direct sales agents and 4800 independent sales agents'}, 'Product Portfolio': {'Categories': 'Polyester textile, fibre intermediates, plastics, petrochemicals, petroleum refining, oil and gas exploration', 'Assortment Size': 'No information available', 'Private Labels': 'No information available'}, 'Customer Segments Served': {'Geographic': 'Rural and urban areas across India, with a presence in over 50000 merchants across major cities', 'Demographic': 'No information available'}, 'Marketing Strategy and Media Presence': {'Pricing Strategy': 'Innovative pricing to drive penetration, with pricing offers and promotions', 'Advertising': 'No information available', 'Social Media': 'No information available'}, 'Affordability Offerings': {'Financing': 'No information available', 'Exchange': 'No information available'}, 'After-Sales Offerings': {'Customer Service': '4800 well-experienced customer care executives across different zones of their network', 'Recycling/Disposal': 'No information available'}, 'Supply Chain': {'Network': 'Reliance Logistics provides transportation, distribution, warehousing, and supply chain services', 'Delivery Promises': 'No information available'}, 'Use of Technology': {'Modern Technologies': 'Used at retail outlets to provide a good customer experience', 'Other Technologies': 'No information available'}}
# business_data = 
# # BusinessModel(**business_data)
# print(BusinessModel(**business_data))

# geographical_data = {'geographical_presence': {'number_of_stores': 7100, 'store_location': 'all over India', 'new_store_additions': None, 'future_store_plans': None, 'store_types': None, 'store_formats': None, 'space_used_for_advertising': None, 'international_presence': 'business over five continents', 'rural_presence': 'business outlets even in rural areas'}}
# geographical_data = {"_".join(key.lower().split()): value for key, value in geographical_data["geographical_presence"].items()}
# print(GeographicalPresence(**geographical_data))