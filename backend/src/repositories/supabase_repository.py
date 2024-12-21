import sys
import os

# Dynamically add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config.supabase_client import SupabaseConfig

from src.config.supabase_client import SupabaseConfig

from src.models.database_models import TravelPackage, Customer

class SupabaseRepository:
    def __init__(self):
        config = SupabaseConfig()
        self.client = config.client

    async def get_travel_packages(self):
        response = self.client.table("travel_packages").select("*").execute()
        if response.error:
            raise Exception(response.error.message)
        return [TravelPackage(**item) for item in response.data]

    async def create_package(self, package_data: dict):
        response = self.client.table("travel_packages").insert(package_data).execute()
        if response.error:
            raise Exception(response.error.message)
        return TravelPackage(**response.data[0])

    async def get_customers_by_agent(self, agent_id: str):
        response = self.client.table("customers").select("*").eq("agent_id", agent_id).execute()
        if response.error:
            raise Exception(response.error.message)
        return [Customer(**item) for item in response.data]
