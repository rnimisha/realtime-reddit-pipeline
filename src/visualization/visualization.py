import pandas as pd
import streamlit as st

from src.config.settings import settings
from src.visualization.charts.metrics_card import get_metrics_card
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


def create_dashboard(df: pd.DataFrame):
    get_metrics_card(st, df)


data = collection.find()
df = pd.DataFrame(list(data))
df["created_at"] = pd.to_datetime(df["created_at"])

create_dashboard(df)
