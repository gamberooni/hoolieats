import pages.cprofile
import pages.rating_behavior
import pages.rprofile
import streamlit as st
from config.config import *
from utils.common import init_postgres_conn
from utils.multiapp import MultiApp

st.set_page_config(layout="wide")

app = MultiApp()
app.add_app("Restaurant Profile", pages.rprofile.app)
app.add_app("Customer Profile", pages.cprofile.app)
app.add_app("Customer Rating Behavior", pages.rating_behavior.app)

conn = init_postgres_conn(
    postgres_host, postgres_port, postgres_database, postgres_user, postgres_password
)
cur = conn.cursor()
cur.execute("CREATE EXTENSION IF NOT EXISTS tablefunc;")  # to use crosstab
conn.commit()
conn.close()

app.run()
