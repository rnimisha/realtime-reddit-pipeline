import plotly.express as px
from pandas import DataFrame


def get_upvote_sentiment_ratio(
    df: DataFrame, custom_theme: str, color_discrete_sequence
):
    scatter_fig = px.scatter(
        df,
        x="upvote_ratio",
        y="sentiment",
        color="sentiment",
        title="Upvote Ratio vs. Sentiment",
        labels={"upvote_ratio": "Upvote Ratio", "sentiment": "Sentiment"},
        template=custom_theme,
        color_discrete_sequence=color_discrete_sequence,
    )
    return scatter_fig
