from dotenv import load_dotenv
import os
from supabase import create_client, Client

class SupabaseConfig:
    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        if not self.url or not self.key:
            raise ValueError("Supabase URL or API Key is not set in the environment variables.")
        self.client = self._initialize_client()

    def _initialize_client(self) -> Client:
        return create_client(self.url, self.key)
