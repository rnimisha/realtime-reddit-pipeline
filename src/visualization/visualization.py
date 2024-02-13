import pandas as pd
import plotly.express as px
import streamlit as st

from src.config.settings import settings
from src.visualization.charts.metrics_card import get_metrics_card
from src.visualization.charts.sentiment_radar_chart import get_sentiment_radar_chart
from src.visualization.charts.upvote_sentiment_ratio import get_upvote_sentiment_ratio
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

# theme
custom_theme = "ggplot2"
color_discrete_sequence = px.colors.sequential.Sunsetdark

# settings
st.set_page_config(
    page_title="Samsung Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
)
st.title(":bar_chart: Samsung Dashboard")

# data
data = collection.find()
df = pd.DataFrame(list(data))
df["created_at"] = pd.to_datetime(df["created_at"])


# dashboard
def create_dashboard(df: pd.DataFrame):
    # first row
    get_metrics_card(st, df)

    # second row
    col1, col2 = st.columns([2, 1])

    with col1:
        upvote_sentiment_ratio = get_upvote_sentiment_ratio(
            df, custom_theme, color_discrete_sequence
        )
        st.plotly_chart(upvote_sentiment_ratio, use_container_width=True)

    with col2:
        sentiment_radar_chart = get_sentiment_radar_chart(df)
        st.plotly_chart(sentiment_radar_chart, use_container_width=True)


create_dashboard(df)
