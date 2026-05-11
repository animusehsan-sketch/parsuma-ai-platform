from typing import List, Dict, Any
import numpy as np

class Evaluator:
    """Calculates performance and quality metrics for the RAG system."""
    
    @staticmethod
    def calculate_retrieval_confidence(scores: List[float]) -> float:
        """Calculate aggregate confidence based on similarity scores."""
        if not scores:
            return 0.0
        return float(np.mean(scores))

    @staticmethod
    def estimate_hallucination_risk(grounding_score: float, confidence: float) -> float:
        """Estimate risk of hallucination (0 to 1)."""
        # Risk is higher when grounding is low and confidence is high (overconfidence)
        # or when both are low.
        risk = 1.0 - (grounding_score * 0.7 + confidence * 0.3)
        return round(float(risk), 2)

    @staticmethod
    def format_metrics(total_tokens: int, latency: float) -> Dict[str, Any]:
        """Format operational metrics."""
        return {
            "token_usage": total_tokens,
            "latency_seconds": round(latency, 2),
            "cost_estimate": round(total_tokens * 0.00002, 5) # Rough estimate for GPT-4
        }
