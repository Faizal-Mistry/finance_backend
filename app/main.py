from fastapi import FastAPI
from app.db import Base, engine
from app.routes import transaction_routes, summary_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Tracking System")

@app.get("/")
def root():
    return {"message": "Finance API is running 🚀"}

app.include_router(transaction_routes.router)
app.include_router(summary_routes.router)