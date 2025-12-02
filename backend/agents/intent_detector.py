# backend/agents/intent_detector.py
from ..llm_providers import generate_openai

INTENT_PROMPT = """
Classify the intent of this email request (choose one): [cold_outreach, follow_up, reply, meeting_request, thank_you, apology, info_share]
Provide only the label.
---
{context}
"""

def detect_intent(context_text):
    prompt = INTENT_PROMPT.format(context=context_text)
    label = generate_openai(prompt, model="gpt-4o-mini", temperature=0)
    return label.strip()
