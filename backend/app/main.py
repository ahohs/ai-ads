import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings

start_time = time.time()

app = FastAPI(title=settings.app_name, version=settings.version)

origins = [o.strip() for o in settings.cors_origins.split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "env": settings.app_env,
        "version": settings.version,
        "uptime_s": int(time.time() - start_time),
    }
