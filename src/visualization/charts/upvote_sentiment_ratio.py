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
        title="Upvote Ratio & Sentiment",
        labels={"upvote_ratio": "Upvote Ratio", "sentiment": "Sentiment"},
        template=custom_theme,
        color_discrete_sequence=color_discrete_sequence,
    )
    scatter_fig.update_layout(
        legend_title_text="",
        legend=dict(
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            orientation="h",
        ),
    )
    return scatter_fig
