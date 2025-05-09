# backend/app/main.py

from fastapi import FastAPI
from app.core.config import settings
from app.api import api_router  # ✅ Importa el router de rutas

app = FastAPI(title=settings.APP_NAME)

# Incluir las rutas registradas en el api_router con el prefijo /api
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": f"Bienvenido a {settings.APP_NAME}"}





