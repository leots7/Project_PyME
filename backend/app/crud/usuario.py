from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models.usuario import Usuario  # Importación absoluta
from app.schemas.usuario import UsuarioCreate

# Configurar el contexto de hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para hashear la contraseña
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Crear un nuevo usuario
def crear_usuario(db: Session, usuario: UsuarioCreate):
    hashed_password = hash_password(usuario.password)
    db_usuario = Usuario(nombre=usuario.nombre, email=usuario.email, hashed_password=hashed_password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Obtener un usuario por su correo
def obtener_usuario_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

# Obtener todos los usuarios
def obtener_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()

