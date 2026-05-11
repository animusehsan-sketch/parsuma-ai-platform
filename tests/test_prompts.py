from src.prompts import RAG_SYSTEM_PROMPT, CONTENT_STRATEGY_PROMPT, SAFETY_EVAL_PROMPT

def test_prompts_not_empty():
    """Ensure all core prompts are defined and non-empty."""
    assert len(RAG_SYSTEM_PROMPT) > 100
    assert len(CONTENT_STRATEGY_PROMPT) > 100
    assert len(SAFETY_EVAL_PROMPT) > 100

def test_prompt_keywords():
    """Check for essential keywords in prompts."""
    assert "Parsuma" in RAG_SYSTEM_PROMPT
    assert "context" in RAG_SYSTEM_PROMPT
    assert "strategy" in CONTENT_STRATEGY_PROMPT
    assert "Grounding" in SAFETY_EVAL_PROMPT
