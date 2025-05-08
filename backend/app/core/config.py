from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    APP_NAME: str = "Proyect_PyME"
    DEBUG: bool = True

    class Config:
        env_file = ".env"  # Asegúrate de que .env esté en la raíz del proyecto

settings = Settings()  # Instancia de la configuración para usar en todo el proyecto
