from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

import os

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = AsyncIOMotorClient(MONGO_URI)

async def connect_db():
    try:
    
        database = client[DB_NAME]

        await init_beanie(database=database, document_models=[])
        print("Database connected successfully!", client.address)
        return client
    except Exception as e:
        print(f"Data base connection failed: {e}")
        raise



