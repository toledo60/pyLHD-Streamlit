import streamlit as st
from pages import generate_LHD
from pages import evaluate_LHD
from pages.misc import MultiPage


# Create an instance of the app 
app = MultiPage()
# Title of the main page
st.sidebar.title("pyLHD")
st.sidebar.text("Latin Hypecubes for Python")

# Add all your applications (pages) here
app.add_page("Generate LHD", generate_LHD.app)
app.add_page('Evaluate LHD', evaluate_LHD.app)

app.run()