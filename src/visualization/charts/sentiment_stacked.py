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
    fig.update_layout(
        legend_title_text="",
        legend=dict(
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            orientation="h",
        ),
    )
    return fig
