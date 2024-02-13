import time

import pandas as pd
import plotly.express as px
import streamlit as st

from src.config.settings import settings
from src.visualization.charts.metrics_card import get_metrics_card
from src.visualization.charts.sentiment_pie_chart import get_sentiment_pie_chart
from src.visualization.charts.sentiment_radar_chart import get_sentiment_radar_chart
from src.visualization.charts.sentiment_stacked import get_sentiment_stacked
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
color_discrete_sequence = px.colors.sequential.Aggrnyl

# settings
st.set_page_config(
    page_title="User Sentiment Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
)
st.title(":bar_chart: User Sentiment Dashboard")


def fetch_new_data():
    data = collection.find()
    df = pd.DataFrame(list(data))
    df["created_at"] = pd.to_datetime(df["created_at"])
    return df


def create_dashboard():

    col1, col2, col3 = st.columns(3)
    negative_placeholder = col3.empty()
    positive_placeholder = col1.empty()
    netural_placeholder = col2.empty()

    first_col1, first_col2 = st.columns([2, 1])
    upvote_sentiment_ratio_placeholder = first_col1.empty()
    sentiment_radar_chart_placeholder = first_col2.empty()

    second_col1, second_col2 = st.columns([1, 2])
    sentiment_pie_chart_placeholder = second_col1.empty()
    sentiment_stacked_placeholder = second_col2.empty()

    while True:
        df = fetch_new_data()

        get_metrics_card(
            col1,
            col2,
            col3,
            positive_placeholder,
            netural_placeholder,
            negative_placeholder,
            df,
        )

        # second row
        with first_col1:
            upvote_sentiment_ratio = get_upvote_sentiment_ratio(
                df, custom_theme, color_discrete_sequence
            )
            upvote_sentiment_ratio_placeholder.plotly_chart(
                upvote_sentiment_ratio, use_container_width=True
            )

        with first_col2:
            sentiment_radar_chart = get_sentiment_radar_chart(df)
            sentiment_radar_chart_placeholder.plotly_chart(
                sentiment_radar_chart, use_container_width=True
            )

        with second_col1:
            sentiment_pie_chart = get_sentiment_pie_chart(
                df, custom_theme, color_discrete_sequence
            )
            sentiment_pie_chart_placeholder.plotly_chart(
                sentiment_pie_chart, use_container_width=True
            )

        with second_col2:
            sentiment_stacked = get_sentiment_stacked(df, color_discrete_sequence)
            sentiment_stacked_placeholder.plotly_chart(
                sentiment_stacked, use_container_width=True
            )

        time.sleep(0.5)


if __name__ == "__main__":
    create_dashboard()
