import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
from plotly.offline import plot


def plot_html(df, title):
    # df = df_from_sql_query(crypto, "Date", conn, startDate, endDate)

    # df["date"] = pd.to_datetime(df["date"])

    df = df.drop(columns=["adj_close"])

    #     eth_df.set_index('Date')

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.07,
        subplot_titles=("OHLC", "Volume"),
        row_width=[0.2, 0.7],
    )

    # Plot OHLC on 1st row
    fig.add_trace(
        go.Candlestick(
            x=df["date"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
            showlegend=False,
        ),
        row=1,
        col=1,
    )

    fig.update_layout(
        xaxis_rangeslider_visible=False,
        template="plotly_dark",
        # plot_bgcolor="rgba(0, 0, 0, 0)",
        # paper_bgcolor="rgba(0, 0, 0, 0)",
    )

    fig.update_layout(
        title=title.upper(),
        yaxis_title="Price",
        autosize=True,
        # width=500,
        height=800,
        margin=dict(l=50, r=50, b=100, t=100, pad=1),
    )

    fig.update_xaxes(
        mirror=True,
        ticks="outside",
        showline=True,
        # linecolor="grey",
        # gridcolor="grey",
        title_standoff=0,
        gridwidth=0.2,
        linewidth=0.1,
    )
    fig.update_yaxes(
        mirror=True,
        ticks="outside",
        showline=True,
        # linecolor="grey",
        # gridcolor="grey",
        title_standoff=10,
        gridwidth=0.2,
        linewidth=0.1,
    )

    def SetColor(df):
        color = []
        for i in df.index:
            if df["close"][i] > df["open"][i]:
                color.append("green")
            else:
                color.append("red")

        return color

    # Bar trace for volumes on 2nd row without legend
    fig.add_trace(
        go.Bar(
            x=df["date"],
            y=df["volume"],
            showlegend=False,
            marker=dict(color=SetColor(df)),
        ),
        row=2,
        col=1,
    )

    fig.update_layout(
        annotations=[
            go.layout.Annotation(
                {
                    "yshift": 10,
                    "font": dict(
                        # family="Courier New, monospace",
                        size=18,
                        # color="#ffffff"
                    ),
                }
            )
        ],
    )

    return fig.to_html()

    # fig.write_html(title + ".html")
    # fig.write_html(title + ".html")

    # fig.show()
