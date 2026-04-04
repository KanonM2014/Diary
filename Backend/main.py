from api.Dairy import Router as Diary_router
from fastapi import FastAPI
app=FastAPI(
    title="====Diary====",
    summary="Aplikasi ini untuk mencatat semua Diary.",
    description="Aplikasi untuk menulis Diary harian.",
    version="1.0.0"
)

app.include_router(router=Diary_router,tags=["Diary"])