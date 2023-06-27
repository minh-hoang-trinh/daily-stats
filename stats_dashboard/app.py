import streamlit as st
from api import get_daily_stats
import datetime
import pandas as pd

st.title("Daily Stats Dashboard")

start_date = st.sidebar.date_input(
    "Start date",
    value=datetime.datetime(2023, 6, 23),
    min_value=datetime.datetime(2023, 6, 23),
    max_value=datetime.datetime.now(),
)

end_date = st.sidebar.date_input(
    "End date",
    value=datetime.datetime.now(),
    max_value=datetime.datetime.now(),
    min_value=start_date,
)


def draw_trend_df(df: pd.DataFrame):
    clone_df = df.copy().T
    clone_df["trend"] = clone_df.apply(lambda x: x.tolist(), axis=1)

    column_config = {
        "trend": st.column_config.LineChartColumn("Trend"),
    }

    column_order = ["trend", *clone_df.columns[:-1]]

    st.data_editor(
        clone_df, column_config=column_config, disabled=True, column_order=column_order
    )


with st.spinner(text="Fetching daily stats..."):
    amounts_df, counters_df = get_daily_stats(start_date=start_date, end_date=end_date)

    counters_tab, amounts_tab = st.tabs(["Counters", "Amounts"])

    with counters_tab:
        draw_trend_df(counters_df)

        st.line_chart(
            counters_df["accountCreatedCount"]
            .cumsum()
            .rename("Cumulative account created"),
        )

        st.bar_chart(
            counters_df["cardCreatedCount"].rename("Card created"),
        )

    with amounts_tab:
        draw_trend_df(amounts_df)

        st.bar_chart(
            amounts_df,
            y=[
                "accountCreditedAmount",
                "accountDebitedAmount",
                "accountForceDebitedAmount",
            ],
        )
