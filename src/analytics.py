import pandas as pd
import json
import os
from datetime import datetime
from typing import List, Dict, Any

class AnalyticsManager:
    """Manages system metrics and query logs for the dashboard."""
    
    def __init__(self, log_path: str = "logs/analytics.json"):
        self.log_path = log_path
        self._ensure_log_file()

    def _ensure_log_file(self):
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        if not os.path.exists(self.log_path):
            with open(self.log_path, 'w') as f:
                json.dump([], f)

    def log_query(self, query_data: Dict[str, Any]):
        """Append query results to analytics log."""
        try:
            with open(self.log_path, 'r') as f:
                logs = json.load(f)
            
            query_data["timestamp"] = datetime.now().isoformat()
            logs.append(query_data)
            
            with open(self.log_path, 'w') as f:
                json.dump(logs, f)
        except Exception as e:
            from .logger import logger
            logger.error(f"Failed to log analytics: {str(e)}")

    def get_dataframe(self) -> pd.DataFrame:
        """Return analytics as a pandas DataFrame."""
        try:
            with open(self.log_path, 'r') as f:
                logs = json.load(f)
            return pd.DataFrame(logs)
        except Exception:
            return pd.DataFrame()

    def get_summary_metrics(self) -> Dict[str, Any]:
        """Calculate high-level KPIs for the overview dashboard."""
        df = self.get_dataframe()
        if df.empty:
            return {
                "total_queries": 0,
                "avg_confidence": 0.0,
                "avg_latency": 0.0,
                "total_tokens": 0
            }
            
        return {
            "total_queries": len(df),
            "avg_confidence": df.get("confidence", pd.Series([0])).mean(),
            "avg_latency": df.get("latency", pd.Series([0])).mean(),
            "total_tokens": df.get("total_tokens", pd.Series([0])).sum()
        }
