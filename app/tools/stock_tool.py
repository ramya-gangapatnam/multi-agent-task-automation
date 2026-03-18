import yfinance as yf


def truncate_text(text: str, max_length: int = 500) -> str:
    """
    Truncate long text to keep tool output compact for downstream agents.
    """
    if not text:
        return ""
    text = text.strip()
    if len(text) <= max_length:
        return text
    return text[:max_length].rstrip() + "..."


def get_stock_data(symbol: str) -> dict:
    """
    Fetch basic stock data using yfinance and return a compact, structured result.
    """
    try:
        clean_symbol = symbol.strip().upper()
        ticker = yf.Ticker(clean_symbol)
        info = ticker.info or {}

        return {
            "symbol": clean_symbol,
            "company_name": info.get("longName") or info.get("shortName"),
            "current_price": info.get("currentPrice"),
            "market_cap": info.get("marketCap"),
            "pe_ratio": info.get("trailingPE"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "summary": truncate_text(info.get("longBusinessSummary", ""), max_length=500),
        }
    except Exception as e:
        return {
            "symbol": symbol,
            "error": str(e),
        }