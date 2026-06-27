from fastapi import FastAPI

from app.api.users import router as users_router
from app.api.notes import router as notes_router

app = FastAPI(
    title="Notes API",
    version="1.0.0"
)

app.include_router(users_router)
app.include_router(notes_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Notes API"
    }