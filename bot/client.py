import os

from dotenv import load_dotenv
from binance.client import Client

from bot.logging_config import setup_logger


logger = setup_logger()

load_dotenv()


class BinanceClient:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            logger.error("API credentials not found.")
            raise ValueError(
                "API_KEY and API_SECRET must be set in the .env file."
            )

        self.client = Client(
            api_key=api_key,
            api_secret=api_secret,
        )

        # Use Binance Futures Testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Connected to Binance Futures Testnet.")

    def get_client(self):
        return self.client
    
client = BinanceClient().get_client()