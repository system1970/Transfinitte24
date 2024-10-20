from pydantic_models import CompetitiveIntelligence

def analyze_insights(insights):
    analysis_result = {}

    # Analyzing business model, geographical presence, performance trends, etc.
    analysis_result["Business Model"] = insights.business_model if insights.business_model else "No data available"
    analysis_result["Geographical Presence"] = insights.geographical_presence if insights.geographical_presence else "No data available"
    analysis_result["Performance Trends"] = insights.performance_trends if insights.performance_trends else "No data available"

    # Handling strategic initiatives as a list of tuples
    if insights.strategic_initiatives:
        si = insights.strategic_initiatives
        analysis_result["Strategic Initiatives"] = f"Investment: {si.investments}, Acquisition: {si.acquisitions}, Other: {si.other_initiatives}"
    else:
        analysis_result["Strategic Initiatives"] = "No data available"

    analysis_result["Future Outlook"] = insights.future_outlook if insights.future_outlook else "No data available"

    return analysis_result

