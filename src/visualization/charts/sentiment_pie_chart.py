import plotly.express as px
from pandas import DataFrame


def get_sentiment_pie_chart(df: DataFrame, custom_theme: str, color_discrete_sequence):
    fig = px.pie(
        df,
        names="emotion",
        title="Emotion Distribution Pie Chart",
        template=custom_theme,
        color_discrete_sequence=color_discrete_sequence,
    )
    return fig
