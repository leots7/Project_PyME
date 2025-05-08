import os

# Estructura de carpetas
structure = {
    "backend": [
        "app",
        "app/api",
        "app/models",
        "app/schemas",
        "app/crud",
        "app/db",
        "app/core",
        "tests"
    ],
    "frontend": [
        "components",
        "pages",
        "services",
        "public"
    ],
    "ai_agent": [
        "prompts",
        "chains",
        "tools"
    ]
}

# Archivos con contenido predeterminado
files_with_content = {
    ".gitignore": """venv/
__pycache__/
*.pyc
.env
.env.*
.idea/
*.sqlite3
""",

    ".env": """# Variables de entorno
DATABASE_URL=sqlite:///./app.db
APP_NAME=Proyect_PyME
DEBUG=True
""",

    "README.md": """# Proyect_PyME

Plataforma web para administración PyME, con backend en FastAPI.
""",

    "docker-compose.yml": """version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    env_file:
      - .env
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
""",

    "backend/requirements.txt": """fastapi
uvicorn[standard]
sqlalchemy
pydantic
python-dotenv
""",

    "backend/app/main.py": '''from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

@app.get("/")
def root():
    return {"message": f"Bienvenido a {settings.APP_NAME}"}
''',

    "backend/app/core/config.py": '''from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    APP_NAME: str = "Proyect_PyME"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
''',

    "backend/app/db/session.py": '''from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
''',

    "backend/app/api/routes.py": '''from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def status():
    return {"status": "OK"}
''',

    "backend/app/api/__init__.py": '''from fastapi import APIRouter
from app.api import routes

api_router = APIRouter()
api_router.include_router(routes.router, prefix="/api")
'''
}

# Crear carpetas
for root, folders in structure.items():
    for folder in folders:
        path = os.path.join(root, folder)
        os.makedirs(path, exist_ok=True)
        # Crear __init__.py en carpetas de Python
        if root == "backend" and folder.startswith("app"):
            init_path = os.path.join(path, "__init__.py")
            with open(init_path, "w", encoding="utf-8") as f:
                f.write("")

# Crear archivos
for path, content in files_with_content.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Proyecto Proyect_PyME inicializado con estructura completa.")
