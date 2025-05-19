import streamlit as st
from model import Model

st.title("Business Idea Generator 💡")
st.subheader("Generate Taglines, Web Domains, Marketing strategies: List of marketing strategies and Competitors")
categories: tuple = ("Food and Beverage", "Clothing and Apparals", "Healthcare and Fitness", "Education", "Social Impact", "Environmental Impact", "Technology and Hardware", "Others")

category: str = st.sidebar.selectbox("Pick a business category", categories)
idea: str = st.text_input(label="Enter a business idea", placeholder="Ex: Airlines Company")