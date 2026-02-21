from fastapi import FastAPI
from database.db import engine, Base
from routes.routes import router
from services.rag import router as rag_router
from dotenv import load_dotenv

load_dotenv()

Base.metadata.create_all(bind=engine)

api = FastAPI(title="College Event Registration  System")

api.include_router(router)
api.include_router(rag_router)
