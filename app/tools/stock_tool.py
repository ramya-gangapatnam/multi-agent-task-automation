import yfinance as yf


def get_stock_data(symbol: str) -> dict:
    """
    Fetch basic stock data using yfinance.
    """
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        return {
            "symbol": symbol,
            "current_price": info.get("currentPrice"),
            "market_cap": info.get("marketCap"),
            "pe_ratio": info.get("trailingPE"),
            "summary": info.get("longBusinessSummary"),
        }
    except Exception as e:
        return {"error": str(e)}