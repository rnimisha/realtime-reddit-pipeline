import plotly.graph_objects as go
from pandas import DataFrame


def get_sentiment_radar_chart(data: DataFrame):
    sentiments = data["sentiment"].unique()

    counts = []
    for sentiment in sentiments:
        count = len(data[data["sentiment"] == sentiment])
        counts.append(count)

    fig = go.Figure(
        data=go.Scatterpolar(
            r=counts,
            theta=sentiments,
            fill="toself",
            line=dict(color="yellow", width=2, shape="linear"),
        )
    )

    fig.update_layout(
        polar=dict(
            bgcolor="black",
            radialaxis=dict(visible=True),
        ),
        showlegend=False,
        title=dict(
            text="Sentiment Radar Chart",
            font=dict(size=18, color="white"),
        ),
    )
    return fig
