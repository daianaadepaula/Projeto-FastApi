# src/app/core/security.py
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Gera o hash seguro da senha (truncando para 72 bytes conforme limite do bcrypt).
    """
    # Garante que é string e corta se necessário
    password = str(password)
    if len(password.encode("utf-8")) > 72:
        password = password.encode("utf-8")[:72].decode("utf-8", errors="ignore")
    return bcrypt_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica se a senha informada confere com o hash armazenado.
    """
    plain_password = str(plain_password)
    if len(plain_password.encode("utf-8")) > 72:
        plain_password = plain_password.encode("utf-8")[:72].decode("utf-8", errors="ignore")
    return bcrypt_context.verify(plain_password, hashed_password)
