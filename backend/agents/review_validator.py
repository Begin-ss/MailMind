# backend/agents/review_validator.py
from ..llm_providers import generate_openai

VALIDATOR_PROMPT = """
Rate the email for grammar, coherence, and tone alignment to {tone} on a 0-100 scale.
Return JSON: {{ "grammar":int, "coherence":int, "tone_alignment":int, "suggestions":[...]}}

Email:
{email}
"""

def validate(email_text, tone="formal"):
    prompt = VALIDATOR_PROMPT.format(tone=tone, email=email_text)
    resp = generate_openai(prompt, model="gpt-4o-mini")
    # Ideally parse JSON from LLM; for POC wrap in try/except
    return resp
