from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from typing import List, Optional
import os
from datetime import datetime
from pydantic import BaseModel

# Models
class TravelPackage(BaseModel):
    id: Optional[int]
    title: str
    description: str
    destination: str
    price: float
    duration: int
    created_at: Optional[datetime]

class Customer(BaseModel):
    id: Optional[int]
    name: str
    email: str
    preferences: dict
    agent_id: int

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

# Dependencies
async def get_supabase():
    return supabase

# Routes
@app.get("/packages/", response_model=List[TravelPackage])
async def get_packages(supabase: Client = Depends(get_supabase)):
    response = supabase.table("packages").select("*").execute()
    return response.data

@app.post("/packages/", response_model=TravelPackage)
async def create_package(package: TravelPackage, supabase: Client = Depends(get_supabase)):
    response = supabase.table("packages").insert(package.dict(exclude={'id'})).execute()
    return response.data[0]

@app.get("/customers/", response_model=List[Customer])
async def get_customers(agent_id: int, supabase: Client = Depends(get_supabase)):
    response = supabase.table("customers").select("*").eq("agent_id", agent_id).execute()
    return response.data

@app.post("/customers/", response_model=Customer)
async def create_customer(customer: Customer, supabase: Client = Depends(get_supabase)):
    response = supabase.table("customers").insert(customer.dict(exclude={'id'})).execute()
    return response.data[0]