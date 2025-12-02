# backend/agents/draft_writer.py
from ..llm_providers import generate_openai

DRAFT_PROMPT = """
You are MailMind, an AI email assistant. Using metadata below, create a complete email (subject + body).
Metadata:
- subject: {subject}
- recipient_name: {recipient_name}
- recipient_type: {recipient_type}
- context: {context}
- required_tone: {tone}

Produce:
Subject: <one-line subject>
Body: <email body>
"""
def generate_draft(metadata):
    prompt = DRAFT_PROMPT.format(**metadata)
    draft = generate_openai(prompt, model="gpt-4o")
    return draft
