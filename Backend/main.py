from Backend.api.Dairy import Router as Diary_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app=FastAPI(
    title="====Diary====",
    summary="Aplikasi ini untuk mencatat semua Diary.",
    description="Aplikasi untuk menulis Diary harian.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=Diary_router,tags=["Diary"])

frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Frontend")
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join(frontend_dir, "index.html"))