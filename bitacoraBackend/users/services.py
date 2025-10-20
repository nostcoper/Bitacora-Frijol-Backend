from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserService:
    @staticmethod
    def register_user(username: str, email: str, password: str, first_name: str = "", last_name: str = "", **extra_fields):
        if User.objects.filter(username=username).exists():
            raise ValidationError("El nombre de usuario ya está en uso.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("El correo electrónico ya está registrado.")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        return user

    @staticmethod
    def authenticate_user(username: str, password: str):
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError("Credenciales inválidas.")

        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        }

    @staticmethod
    def get_profile(user_id: int):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError("Usuario no encontrado.")
