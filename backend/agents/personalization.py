# backend/agents/personalization.py
from ..storage import get_profile

def personalize(draft_text, user_id, recipient_profile=None):
    profile = get_profile(user_id) or {}
    if recipient_profile:
        draft_text = draft_text.replace("{recipient_name}", recipient_profile.get("name",""))
    # apply sender signature / style prefs
    style = profile.get("style_notes")
    if style:
        draft_text += f"\n\n{style}"
    return draft_text
