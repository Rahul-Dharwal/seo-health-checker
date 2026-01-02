import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="One-Click SEO", page_icon="📈")
st.title("📈 One-Click SEO Analyzer")

url = st.text_input("Enter URL to audit:", "https://")

if st.button("Start Audit"):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        st.subheader("Results")
        st.write(f"**Title:** {soup.title.string if soup.title else '❌ Missing'}")
        st.write(f"**H1 Tag:** {soup.h1.text if soup.h1 else '❌ Missing'}")
        st.success("SEO Audit Finished!")
    except:
        st.error("Please enter a valid URL.")