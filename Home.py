import streamlit as st

st.set_page_config(page_title="Home", page_icon="🌍")

st.title("World Cities")
st.write(
    "Welcome to the World Cities app! Explore city data, discover insights, and navigate to the main application page."
)

if st.button("Go to App"):
    st.switch_page("pages/app.py")
