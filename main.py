import streamlit as st
from app.query_llm import query_llama3_ollama
from app.extract import extract_brands
from app.visualize import show_results

st.set_page_config(page_title="LLM Brand Analyzer", layout="wide")
st.title("🤖 LLM Brand Perception Analyzer")

category = st.text_input("Enter a product category (e.g., luxury skincare, fitness apps)")

if st.button("Analyze with Mistral") and category:
    with st.spinner("Querying Mistral..."):
        response = query_llama3_ollama(category)
        brand_data = extract_brands(response)
        show_results(brand_data)
