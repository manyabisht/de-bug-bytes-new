import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import os
from datetime import datetime
from pydantic import BaseModel

from src.config.supabase_client import SupabaseConfig
from src.models.database_models import TravelPackage, Customer

from src.repositories.supabase_repository import SupabaseRepository

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get Supabase client
supabase_config = SupabaseConfig()

# Dependencies
def get_repository():
    return SupabaseRepository()

@app.get("/")
async def root():
    return {"message": "TBO Travel Agent API is running"}

@app.get("/packages/", response_model=List[TravelPackage])
async def get_packages(repo: SupabaseRepository = Depends(get_repository)):
    try:
        return await repo.get_travel_packages()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/packages/", response_model=TravelPackage)
async def create_package(
    package: TravelPackage, 
    repo: SupabaseRepository = Depends(get_repository)
):
    try:
        return await repo.create_package(package.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/customers/", response_model=List[Customer])
async def get_customers(
    agent_id: str,
    repo: SupabaseRepository = Depends(get_repository)
):
    try:
        return await repo.get_customers_by_agent(agent_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    