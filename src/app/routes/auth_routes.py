from fastapi import APIRouter, HTTPException
from src.app.models.users_models import User

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação de nosso sistema
    """
    return {"message": "Você acessou a rota padrão de autenticação", "authenticate": False}

@auth_router.post("/signup")
async def signup(name: str, email: str, password: str):
    # Verifica se já existe
    existing_user = await User.find_one({"email": email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    # Cria usuário
    new_user = User(name=name, email=email, password=password)
    await new_user.insert()

    return {"message": "Usuário cadastrado com sucesso", "user_id": str(new_user.id)}