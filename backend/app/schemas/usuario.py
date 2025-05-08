from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    password: str

    class Config:
        # Esto asegura que los nombres de las variables sean iguales en el modelo de base de datos y en el esquema
        orm_mode = True
