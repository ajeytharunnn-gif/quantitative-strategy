# =====================================================================
# INSTITUTIONAL QUANTITATIVE ALPHA STRATEGY MODULE
# =====================================================================
import numpy as np

def generate_signals(orderbook_ticks):
    """
    Evaluate incoming Level-2 orderbook ticks and return strategy action.
    Args:
        orderbook_ticks (dict/list): Array of bid/ask prices and depth quantities.
    Returns:
        dict: {"action": "BUY_LONG" | "SELL_SHORT" | "EXIT" | "HOLD", "confidence": float}
    """
    return {"action": "HOLD", "confidence": 0.0}
