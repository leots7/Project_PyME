from core.config import settings  # ✅ Import relativo al paquete `app`

from fastapi import FastAPI

app = FastAPI(title=settings.APP_NAME)

@app.get("/")
def root():
    return {"message": f"Bienvenido a {settings.APP_NAME}"}




