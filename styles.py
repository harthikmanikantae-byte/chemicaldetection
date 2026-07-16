import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        .main {
            background-color: #f8f9fa;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: #ffffff;
            border-radius: 4px 4px 0px 0px;
            gap: 1px;
            padding-top: 10px;
            padding-bottom: 10px;
        }
        .stTabs [aria-selected="true"] {
            background-color: #e9ecef;
            font-weight: bold;
        }
        .metric-card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-left: 5px solid #007bff;
        }
        .paper-card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 15px;
            border: 1px solid #dee2e6;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .paper-title {
            color: #0056b3;
            font-size: 1.1em;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .paper-metadata {
            color: #6c757d;
            font-size: 0.9em;
            margin-bottom: 5px;
        }
        .section-header {
            color: #343a40;
            border-bottom: 2px solid #007bff;
            padding-bottom: 5px;
            margin-top: 20px;
            margin-bottom: 15px;
        }
        .info-label {
            font-weight: bold;
            color: #495057;
        }
        </style>
    """, unsafe_allow_html=True)
