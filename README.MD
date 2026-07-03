# Binance Futures Trading Bot

## Features

- Market Orders
- Limit Orders
- Stop-Limit Orders
- CLI Interface
- Streamlit UI
- Logging
- Validation

## 📂 Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py              # Binance API client
│   ├── config.py              # Configuration settings
│   ├── logging_config.py      # Logging setup
│   ├── orders.py              # Market, Limit & Stop-Limit order logic
│   └── validators.py          # Input validation
│
├── logs/
│   └── trading.log            # API requests, responses & errors
│
├── screenshots/
│   ├── cli.png
│   ├── streamlit.png
│   └── logs.png
│
├── ui/
│   └── app.py                 # Streamlit web interface
│
├── .env.example               # Sample environment variables
├── .gitignore
├── cli.py                     # CLI entry point
├── README.md
└── requirements.txt
```

## 📋 Requirements

- Python 3.10 or later
- Binance Futures Demo/Testnet account
- Binance Demo/Testnet API Key and Secret
- Internet connection
- Required Python packages (listed in `requirements.txt`)

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/nilaksh-parihar/trading_bot.git
cd trading_bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
API_KEY=your_demo_api_key
API_SECRET=your_demo_api_secret
```

> **Note:** Generate your API credentials from the Binance Futures Demo/Testnet environment, not from your regular Binance account.

### 6. Run the CLI

```bash
python cli.py
```

### 7. Run the Streamlit UI

```bash
streamlit run ui/app.py
```

## Configuration

Create a `.env` file in the project root and add your Binance Demo/Testnet API credentials:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

> **Note:** Generate your API credentials from the Binance Futures Demo/Testnet environment, not from your regular Binance account.

## Example

![CLI Screenshot](screenshots/cli.png)
![Streamlit Screenshot](screenshots/ui.png)
![Log Screenshot](screenshots/log.png)

## Logs

logs/trading.log

## Assumptions

- The application uses the Binance Futures Testnet/Demo environment.
- Users have valid Binance Testnet API credentials stored in a `.env` file.
- The trading symbol is valid (e.g., BTCUSDT).
- LIMIT and STOP_LIMIT orders require a valid price.
- The account has sufficient demo balance for order execution.