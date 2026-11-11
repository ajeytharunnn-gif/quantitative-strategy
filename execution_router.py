# =====================================================================
# ORDER EXECUTION & ROUTING ENGINE
# =====================================================================
def execute_order(action: str, volume: float, market_price: float):
    return {"action": action, "volume": volume, "fill_price": market_price, "status": "FILLED"}
