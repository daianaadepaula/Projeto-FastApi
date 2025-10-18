from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def authenticate():
    """
    Essa é a rota padrão de autenticação de nosso sistema
    """
    return {"message": "Você acessou a rota padrão de autenticação", "authenticate": False}