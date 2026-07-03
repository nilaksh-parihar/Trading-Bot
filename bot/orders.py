from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.client import client
from bot.logging_config import setup_logger
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    validate_stop_price,
)

logger = setup_logger()

def place_market_order(symbol, side, quantity):

    symbol = validate_symbol(symbol)
    side = validate_side(side)
    quantity = validate_quantity(quantity)

    try:
        logger.info(
            f"Placing MARKET {side} order | Symbol={symbol} Qty={quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity,
        )

        order = client.futures_get_order(
            symbol=symbol,
            orderId=response["orderId"],
        )

        logger.info(
            f"""
        Order Placed Successfully
        -------------------------
        Order ID : {order['orderId']}
        Symbol   : {order['symbol']}
        Side     : {order['side']}
        Type     : {order['type']}
        Status   : {order['status']}
        Executed : {order['executedQty']}
        Price    : {order.get('avgPrice', 'N/A')}
        """
        )

        return response

    except (BinanceAPIException, BinanceRequestException) as e:
        logger.error(str(e))
        raise

    except Exception as e:
        logger.exception(str(e))
        raise

def place_limit_order(symbol, side, quantity, price):

    symbol = validate_symbol(symbol)
    side = validate_side(side)
    quantity = validate_quantity(quantity)
    price = validate_price(price)

    try:

        logger.info(
            f"Placing LIMIT {side} order | "
            f"Symbol={symbol} Qty={quantity} Price={price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC,
        )

        order = client.futures_get_order(
            symbol=symbol,
            orderId=response["orderId"],
        )

        logger.info(
            f"""
        Order Placed Successfully
        -------------------------
        Order ID : {order['orderId']}
        Symbol   : {order['symbol']}
        Side     : {order['side']}
        Type     : {order['type']}
        Status   : {order['status']}
        Executed : {order['executedQty']}
        Price    : {order.get('avgPrice', 'N/A')}
        """
        )

        return response

    except (BinanceAPIException, BinanceRequestException) as e:
        logger.error(str(e))
        raise

    except Exception as e:
        logger.exception(str(e))
        raise

def place_stop_limit_order(
    symbol,
    side,
    quantity,
    price,
    stop_price,
):

    symbol = validate_symbol(symbol)
    side = validate_side(side)
    quantity = validate_quantity(quantity)
    price = validate_price(price)
    stop_price = validate_stop_price(stop_price)

    try:

        logger.info(
            f"Placing STOP_LIMIT {side} order | "
            f"Symbol={symbol} Qty={quantity} "
            f"Price={price} Stop={stop_price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_STOP,
            quantity=quantity,
            price=price,
            stopPrice=stop_price,
            timeInForce=TIME_IN_FORCE_GTC,
        )

        logger.info(
            f"""
        Order Placed Successfully
        -------------------------
        Order ID : {order['orderId']}
        Symbol   : {order['symbol']}
        Side     : {order['side']}
        Type     : {order['type']}
        Status   : {order['status']}
        Executed : {order['executedQty']}
        Price    : {order.get('avgPrice', 'N/A')}
        """
        )

        return response

    except (BinanceAPIException, BinanceRequestException) as e:
        logger.error(str(e))
        raise

    except Exception as e:
        logger.exception(str(e))
        raise