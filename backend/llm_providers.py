# backend/llm_providers.py
from openai import OpenAI
from anthropic import Anthropic
from google.cloud import aiplatform
from .config import OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_APPLICATION_CREDENTIALS

# ✅ Initialize OpenAI Client
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# ✅ Initialize Anthropic Client (Claude)
anthropic_client = Anthropic(api_key=ANTHROPIC_API_KEY)

# ✅ Initialize Google Vertex AI (Gemini)
aiplatform.init()

# ---------- OPENAI ----------
def generate_openai(prompt, model="gpt-4o-mini", temperature=0.3, max_tokens=512):
    """Generate text using OpenAI models"""
    try:
        response = openai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[OpenAI Error] {str(e)}"

# ---------- ANTHROPIC ----------
def generate_anthropic(prompt, model="claude-3-sonnet-20240229"):
    """Generate text using Anthropic Claude"""
    try:
        response = anthropic_client.messages.create(
            model=model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        return f"[Anthropic Error] {str(e)}"

# ---------- GEMINI ----------
def generate_gemini(prompt, model="gemini-1.5-pro"):
    """Generate text using Google Gemini via Vertex AI"""
    try:
        from vertexai.preview.generative_models import GenerativeModel
        model = GenerativeModel(model)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[Gemini Error] {str(e)}"
