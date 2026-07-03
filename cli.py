import typer
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm

from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_limit_order,
)

console = Console()
app = typer.Typer()

@app.command()
def trade():
    symbol = Prompt.ask("Enter Symbol").upper()

    side = Prompt.ask(
        "Side",
        choices=["BUY", "SELL"],
    )

    order_type = Prompt.ask(
        "Order Type",
        choices=["MARKET", "LIMIT", "STOP_LIMIT"],
    )

    quantity = float(Prompt.ask("Quantity"))

    price = None
    stop_price = None

    if order_type in ["LIMIT", "STOP_LIMIT"]:
        price = float(Prompt.ask("Limit Price"))

    if order_type == "STOP_LIMIT":
        stop_price = float(Prompt.ask("Stop Price"))

    table = Table(title="Order Summary")

    table.add_column("Field")
    table.add_column("Value")

    table.add_row("Symbol", symbol)
    table.add_row("Side", side)
    table.add_row("Type", order_type)
    table.add_row("Quantity", str(quantity))

    if price:
        table.add_row("Price", str(price))

    if stop_price:
        table.add_row("Stop Price", str(stop_price))

    console.print(table)

    if not Confirm.ask("Place this order?"):
        console.print("[yellow]Order cancelled.[/yellow]")
        raise typer.Exit()
    
    try:

        if order_type == "MARKET":
            response = place_market_order(
                symbol,
                side,
                quantity,
            )

        elif order_type == "LIMIT":
            response = place_limit_order(
                symbol,
                side,
                quantity,
                price,
            )

        else:
            response = place_stop_limit_order(
                symbol,
                side,
                quantity,
                price,
                stop_price,
            )

        console.print("\n[green]Order placed successfully![/green]\n")

        table = Table(title="Order Response")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row("Order ID", str(response.get("orderId")))
        table.add_row("Status", response.get("status", "N/A"))
        table.add_row("Executed Qty", response.get("executedQty", "N/A"))
        table.add_row("Average Price", response.get("avgPrice", "N/A"))

        console.print(table)

    except Exception as e:
        console.print(f"[red]{e}[/red]")

if __name__ == "__main__":
    app()