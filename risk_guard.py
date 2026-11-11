# =====================================================================
# INSTITUTIONAL RISK SENTINEL MODULE
# =====================================================================
class RiskGuard:
    def __init__(self, max_drawdown_ceiling=0.025, starting_capital=100000.0):
        self.max_drawdown_ceiling = max_drawdown_ceiling
        self.peak_capital = starting_capital
        self.current_capital = starting_capital

    def evaluate_risk(self, current_capital: float):
        if current_capital > self.peak_capital:
            self.peak_capital = current_capital
        drawdown = (self.peak_capital - current_capital) / max(1.0, self.peak_capital)
        breached = drawdown > self.max_drawdown_ceiling
        return {"drawdown": round(drawdown * 100.0, 2), "breached": breached, "status": "HALT" if breached else "NOMINAL"}
