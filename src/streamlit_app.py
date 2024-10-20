import streamlit as st
import streamlit_shadcn_ui as ui
from streamlit_searchbox import st_searchbox
import extra_streamlit_components as stx
from st_diff_viewer import diff_viewer
import json

import altair as alt

from competitor_list import competitorList
from utils.search_helper import trigram_search
from main import get_analysis
import time

from competitor_list import competitorList
from utils.search_helper import trigram_search
from main import get_analysis
from utils.graph import get_graph_data_for_streamlit
from streamlit_echarts import st_echarts

# Initialize session state variables if they don't exist]
if 'CompareFlag' not in st.session_state:
    st.session_state.CompareFlag = False
if 'DiffFlag' not in st.session_state:
    st.session_state.DiffFlag = False

st.set_page_config(
    page_title="Competitive Analysis Dashboard",
    page_icon="[]",
    layout="wide",
    initial_sidebar_state="expanded"
)

alt.themes.enable("dark")

with st.sidebar:
    st.markdown('# Analysis Dashboard')
    st.markdown("## - Select Competitor")
    selected_value = st_searchbox(
        trigram_search,
        key="competitor_searchbox",
        default_options=trigram_search(""),
    )
    if selected_value is not None:
        compare_mode = ui.switch(default_checked=False, label="Compare Mode", key="compare_mode")

# COMPETITOR NAME
if selected_value is None:
    st.markdown("""
    <style>
    .middle {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
        font-size: 24px;
    }
    </style>
    <div class="middle">
        <h1>Choose A Competitor To Begin Analysis</h1>
    </div>
    """, unsafe_allow_html=True)
else:
    results = get_analysis(selected_value)

    if compare_mode:
        # Create two columns for the select boxes
        name_col1, name_col2 = st.columns(2)
        with name_col1:
            st.markdown(f"<h1>{selected_value}</h1>", unsafe_allow_html=True)
        with name_col2:
            st.markdown("## Select a Company to Compare with: ")
            compare_search_box = st_searchbox(
                trigram_search,
                key="compare_competitor_searchbox",
                default_options=trigram_search(""),
                placeholder="--- None ---"
            )
        if compare_search_box is not None:
            if compare_search_box == selected_value:
                st.title(":red[Warning: Choose A Different Competitor To Compare With]")
                st.session_state.CompareFlag = False
            else:
                compare_results = get_analysis(compare_search_box)
                st.session_state.CompareFlag = True
    else:
        st.markdown(f"<h1 style='text-align: center;margin-bottom: 1vh;'>{selected_value}</h1>", unsafe_allow_html=True)

    if results:
        current_tab = stx.tab_bar(data=[
            stx.TabBarItemData(id=f"{key}", title=f"{key}", description="")
            for key in results.keys()
        ], default="Business Model")
    
        if not st.session_state.compare_mode:
            st.write(results[current_tab])
        else:
            col1, col2 = st.columns(2)
            with col1:
                st.write(results[current_tab])
            with col2:
                if st.session_state.CompareFlag and compare_results:
                    st.write(compare_results[current_tab])

    if selected_value and st.session_state.compare_mode and st.session_state.CompareFlag:
        st.markdown(
            """
            <style>
            .centered {
                display: flex;
                justify-self: center;  /* Center horizontally */
                align-items: center;      /* Center vertically */
                height: 100%;             /* Use full height of the parent */
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        if ui.button(text="View Difference", key="trigger_btn", class_name="centered"):
            st.session_state.DiffFlag = not st.session_state.DiffFlag
            
        if st.session_state.DiffFlag and compare_results:
            check1, check2, check3 = st.columns(3)
            split_view = check1.checkbox("Split View", value=True, key='split_view')
            use_dark_theme = check2.checkbox("Use Dark Theme", value=False, key='use_dark_theme')
            hide_line_numbers = check3.checkbox("Hide Line Numbers", value=False, key='hide_line_numbers')

            col1, col2 = st.columns(2)
            extra_lines_surrounding_diff = col1.number_input("Extra Lines Surrounding Diff", 3, key='extra_lines')
            highlight_lines = col2.text_area("Highlight Lines", "", key='highlight_lines').split("\n")
            
            def pydantic_model_to_formatted_json(model):
                json_string = model.model_dump_json()
                parsed_json = json.loads(json_string)
                formatted_json = json.dumps(parsed_json, indent=4)
                return formatted_json

            diff_viewer(
                old_text=f"{pydantic_model_to_formatted_json(results[current_tab])}",
                new_text=f"{pydantic_model_to_formatted_json(compare_results[current_tab])}",
                split_view=split_view,
                left_title=selected_value,
                right_title=compare_search_box,
                extra_lines_surrounding_diff=extra_lines_surrounding_diff,
                hide_line_numbers=hide_line_numbers,
                highlight_lines=highlight_lines,
            )

    if results[current_tab]:
        try:
            graph_data = get_graph_data_for_streamlit(results[current_tab].model_dump_json())

            if graph_data:
                # Extract x and y data
                x_data = graph_data.get("x_data", [])
                y_data = graph_data.get("y_data", [])

                # Create an Echarts option for plotting
                option = {
                    "xAxis": {
                        "type": "category",
                        "data": x_data
                    },
                    "yAxis": {
                        "type": "value"
                    },
                    "series": [
                        {
                            "data": y_data,
                            "type": "line"  # Use "bar" for bar chart or other types as needed
                        }
                    ]
                }

                # Display the graph using Echarts
                st_echarts(options=option, height="400px")
        except: 
            st.warning("Unable to extract graphable data from the JSON input.")
