import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_limit_order,
)

st.set_page_config(
    page_title="Trading Bot",
    page_icon="📈"
)

st.title("📈 Binance Futures Trading Bot")

symbol = st.text_input(
    "Symbol",
    value="BTCUSDT"
)

side = st.selectbox(
    "Side",
    ["BUY", "SELL"]
)

order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT", "STOP_LIMIT"]
)

quantity = st.number_input(
    "Quantity",
    min_value=0.001,
    value=0.01
)

price = None
stop_price = None

if order_type in ["LIMIT", "STOP_LIMIT"]:
    price = st.number_input(
        "Limit Price",
        min_value=1.0
    )

if order_type == "STOP_LIMIT":
    stop_price = st.number_input(
        "Stop Price",
        min_value=1.0
    )

if st.button("Place Order"):
    try:

        if order_type == "MARKET":
            response = place_market_order(
                symbol,
                side,
                quantity
            )

        elif order_type == "LIMIT":
            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        else:
            response = place_stop_limit_order(
                symbol,
                side,
                quantity,
                price,
                stop_price
            )

        st.success("Order placed successfully!")

        st.subheader("Order Response")

        st.table({
            "Field": [
                "Order ID",
                "Status",
                "Executed Qty",
                "Average Price"
            ],
            "Value": [
                response.get("orderId"),
                response.get("status"),
                response.get("executedQty"),
                response.get("avgPrice"),
            ]
        })

    except Exception as e:
        st.error(str(e))