import pages.rating_behavior
import pages.restaurant_profile
import pages.user_profile
import streamlit as st
from utils.multiapp import MultiApp

st.set_page_config(layout="wide")

app = MultiApp()
app.add_app("Restaurant Profile", pages.restaurant_profile.app)
app.add_app("User Profile", pages.user_profile.app)
# app.add_app("Customer Rating Behavior", pages.rating_behavior.app)

app.run()
