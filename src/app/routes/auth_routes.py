from fastapi import APIRouter, HTTPException
from src.app.models.users_models import User
from src.app.core.security import hash_password
from src.app.schemas.schemas import UserSchema

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação de nosso sistema
    """
    return {"message": "Você acessou a rota padrão de autenticação", "authenticate": False}

@auth_router.post("/signup")
async def signup(user_schema: UserSchema):
    # Verifica se já existe
    existing_user = await User.find_one({"email": user_schema.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    # Cria usuário
    encrypted_password = hash_password(user_schema.password)
    new_user = User(name=user_schema.name, email=user_schema.email, password=encrypted_password, active=user_schema.active, admin=user_schema.admin)
    await new_user.insert()

    return {"message": "Usuário cadastrado com sucesso", "email": str(user_schema.email)}