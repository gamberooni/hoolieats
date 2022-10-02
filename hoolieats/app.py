import pages.cprofile
import pages.rating_behavior
import pages.rprofile
import streamlit as st
from utils.multiapp import MultiApp

st.set_page_config(layout="wide")

app = MultiApp()
# app.add_app("Restaurant Profile", pages.rprofile.app)
app.add_app("Customer Profile", pages.cprofile.app)
# app.add_app("Customer Rating Behavior", pages.rating_behavior.app)

app.run()
