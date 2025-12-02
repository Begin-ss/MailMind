# backend/agents/tone_stylist.py
from ..llm_providers import generate_openai

TONE_PROMPT = """
Rewrite the following email in a {tone} tone, keep length similar and use professional grammar.
Email: {email}
Return only the rewritten email body.
"""

def rewrite_tone(email_text, tone="formal"):
    prompt = TONE_PROMPT.format(tone=tone, email=email_text)
    return generate_openai(prompt, model="gpt-4o-mini")
