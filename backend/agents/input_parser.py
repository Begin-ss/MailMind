# backend/agents/input_parser.py
def parse_input(form_data: dict):
    # form_data from Streamlit UI
    return {
        "subject": form_data.get("subject",""),
        "context": form_data.get("context",""),
        "recipient_type": form_data.get("recipient_type","colleague"),
        "recipient_name": form_data.get("recipient_name",""),
        "tone": form_data.get("tone","friendly"),
        "user_id": form_data.get("user_id")
    }
