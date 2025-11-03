from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.routes.query_route import router as query_route

from app.config.database_config import connect_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
  

app = FastAPI(lifespan=lifespan)

app.add_middleware(
   CORSMiddleware,
   allow_origins= "*",
   allow_credentials=True,
   allow_headers=["*"],
   allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"]
)

app.include_router(query_route, prefix="/api/query")

@app.get('/')
async def mridul():
    return {"message": "Jai sir ram"}