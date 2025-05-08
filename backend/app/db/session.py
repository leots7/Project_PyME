from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings

# Crear motor de base de datos
engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crear fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener una sesión de base de datos
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

