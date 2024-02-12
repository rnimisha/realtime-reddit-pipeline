import pandas as pd
import streamlit as st

from src.config.settings import settings
from src.visualization.db.connect import init_connect

# database
client = init_connect(
    settings.DB_USER,
    settings.DB_PASSWORD,
    settings.DB_HOST,
    settings.DB_PORT,
    settings.DB_DATABASE,
)
db = client[settings.DB_DATABASE]
collection = db["redditstream"]


# settings
st.set_page_config(
    page_title="Samsung Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
)
st.title(":bar_chart: Samsung Dashboard")
