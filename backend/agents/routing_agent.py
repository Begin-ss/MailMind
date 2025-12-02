# backend/agents/routing_agent.py
from ..llm_providers import generate_openai, generate_anthropic

def with_fallback(func, *args, **kwargs):
    # Try primary provider (OpenAI), fallback to Anthropic
    try:
        return func(*args, **kwargs)  # assume this uses OpenAI by default
    except Exception as e:
        print("Primary LLM failed, falling back to Anthropic:", e)
        # minimal example: re-call using Anthropic by temporarily switching provider
        # Implement provider switch inside func or provide alternate wrapper
        return generate_anthropic(kwargs.get("prompt", ""))
