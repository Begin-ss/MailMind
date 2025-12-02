# backend/orchestrator.py
from backend.agents.input_parser import parse_input
from backend.agents.intent_detector import detect_intent
from backend.agents.draft_writer import generate_draft
from backend.agents.tone_stylist import rewrite_tone
from backend.agents.personalization import personalize
from backend.agents.review_validator import validate
from backend.agents.routing_agent import with_fallback

def run_mailmind(form_data):
    meta = parse_input(form_data)
    intent = detect_intent(meta['context'])
    meta['intent'] = intent
    draft_raw = with_fallback(generate_draft, metadata=meta)  # use routing wrapper
    draft_toned = rewrite_tone(draft_raw, tone=meta['tone'])
    draft_personal = personalize(draft_toned, meta['user_id'])
    validation = validate(draft_personal, tone=meta['tone'])
    return {
        "draft": draft_personal,
        "validation": validation
    }
