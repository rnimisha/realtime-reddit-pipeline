from pandas import DataFrame
from streamlit_extras.metric_cards import style_metric_cards


def get_metrics_card(
    col1,
    col2,
    col3,
    positive_placeholder,
    netural_placeholder,
    negative_placeholder,
    df: DataFrame,
):
    sentiment_counts = df["sentiment"].value_counts()

    style_metric_cards(
        background_color="#000",
        border_left_color="#686664",
        border_color="#000000",
        box_shadow="#F71938",
    )

    with col1:
        positive_placeholder.metric(
            label="😄 Positive",
            value=f" {sentiment_counts.get('positive', 0)}",
        )

    with col2:
        netural_placeholder.metric(
            label="😐 Neutral",
            value=f" {sentiment_counts.get('neutral', 0)}",
        )

    with col3:
        negative_placeholder.metric(
            label="😡 Negative",
            value=f" {sentiment_counts.get('negative', 0)}",
        )
