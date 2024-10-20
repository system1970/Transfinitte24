import streamlit as st
from streamlit_pydantic import pydantic_input, pydantic_output
from pydantic_models import CompetitiveIntelligence, BusinessModel, GeographicalPresence, PerformanceTrends, StrategicInitiatives

# Header
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Competitive Intelligence Dashboard</h1>", unsafe_allow_html=True)
st.write("Welcome to the Competitive Intelligence Dashboard. Please fill in the details below:")

# Render input form for Competitive Intelligence
with st.form("competitive_intelligence_form"):
    st.subheader("Business Model")
    business_model = pydantic_input(key = "Business Model Form", model = BusinessModel)

    st.subheader("Geographical Presence")
    geographical_presence = pydantic_input(key = "Geographical Presence Form", model = GeographicalPresence)

    st.subheader("Performance Trends")
    performance_trends = pydantic_input(key = "PerformanceTrends Form", model = PerformanceTrends)

    st.subheader("Strategic Initiatives")
    strategic_initiatives = pydantic_input(key = "Strategic Initiatives Form", model = StrategicInitiatives)

    # Optional future outlook input
    future_outlook = st.text_area("Future Outlook", "Enter future outlook")

    # Submit button
    submit_button = st.form_submit_button(label="Generate Competitive Intelligence")

# Handle the form submission
if submit_button:
    # Create Competitive Intelligence instance
    competitive_intelligence = CompetitiveIntelligence(
        business_model=business_model,
        geographical_presence=geographical_presence,
        performance_trends=performance_trends,
        strategic_initiatives=strategic_initiatives,
        future_outlook=future_outlook
    )

    # Display the output
    st.subheader("Generated Competitive Intelligence Data")
    pydantic_output(competitive_intelligence)
    
# Add footer
st.markdown("""
    <div style='text-align: center; margin-top: 50px;'>
        <p>Powered by <strong>Streamlit</strong> and <strong>Streamlit-Pydantic</strong></p>
    </div>
""", unsafe_allow_html=True)
