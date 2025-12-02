# backend/storage.py
import redis
import json
from .config import REDIS_URL

r = redis.from_url(REDIS_URL, decode_responses=True)

def upsert_profile(user_id, profile: dict):
    r.hset(f"profile:{user_id}", mapping=profile)

def get_profile(user_id):
    data = r.hgetall(f"profile:{user_id}")
    return data or None

def save_email_log(user_id, email_obj):
    r.lpush(f"emails:{user_id}", json.dumps(email_obj))
