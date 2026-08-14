import json
import redis


class RedisService:

    def __init__(self):
        self.client = redis.Redis(
            host="172.17.21.149",
            port=6379,
            db=0,
            decode_responses=True
        )

    def get_history(self, session_id: str):
        data = self.client.get(f"chat:{session_id}")

        if not data:
            return []

        return json.loads(data)

    def save_history(self, session_id: str, history: list):
        self.client.set(
            f"chat:{session_id}",
            json.dumps(history)
        )

    def clear_history(self, session_id: str):
        self.client.delete(f"chat:{session_id}")