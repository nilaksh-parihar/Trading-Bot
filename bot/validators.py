VALID_SIDES = {"BUY", "SELL"}

VALID_ORDER_TYPES = {
    "MARKET",
    "LIMIT",
    "STOP_LIMIT",
}


def validate_symbol(symbol: str) -> str:
    """
    Validate and normalize the trading symbol.
    """
    symbol = symbol.upper().strip()

    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    if not symbol.isalnum():
        raise ValueError("Symbol must contain only letters and numbers.")

    return symbol


def validate_side(side: str) -> str:
    """
    Validate the order side.
    """
    side = side.upper().strip()

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type: str) -> str:
    """
    Validate the order type.
    """
    order_type = order_type.upper().strip()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(
            "Order type must be MARKET, LIMIT, or STOP_LIMIT."
        )

    return order_type


def validate_quantity(quantity: float) -> float:
    """
    Validate the order quantity.
    """
    try:
        quantity = float(quantity)
    except ValueError:
        raise ValueError("Quantity must be a number.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    return quantity


def validate_price(price: float) -> float:
    """
    Validate the limit order price.
    """
    if price is None:
        raise ValueError("Price is required.")

    try:
        price = float(price)
    except ValueError:
        raise ValueError("Price must be a number.")

    if price <= 0:
        raise ValueError("Price must be greater than 0.")

    return price


def validate_stop_price(stop_price: float) -> float:
    """
    Validate the stop price for STOP_LIMIT orders.
    """
    if stop_price is None:
        raise ValueError("Stop price is required.")

    try:
        stop_price = float(stop_price)
    except ValueError:
        raise ValueError("Stop price must be a number.")

    if stop_price <= 0:
        raise ValueError("Stop price must be greater than 0.")

    return stop_price