import plotly.express as px
from pandas import DataFrame


def get_sentiment_stacked(df: DataFrame, color_discrete_sequence):
    fig = px.bar(
        df,
        x="emotion",
        color="sentiment",
        title="Sentiment Distribution by Emotion",
        labels={"emotion": "Emotion", "count": "Count"},
        barmode="stack",
        color_discrete_sequence=color_discrete_sequence,
    )
    return fig
