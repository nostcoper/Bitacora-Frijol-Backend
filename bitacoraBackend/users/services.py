import datetime
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserService:
    @staticmethod
    def register_user(username: str, email: str, password: str, first_name: str = "", last_name: str = "", points:int = 0, **extra_fields):
        if User.objects.filter(username=username).exists():
            raise ValidationError("El nombre de usuario ya está en uso.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("El correo electrónico ya está registrado.")
        print(first_name)
        print(last_name)
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            points = points,
            **extra_fields
        )
        return user

    @staticmethod
    def authenticate_user(username: str, password: str):
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError("Credenciales inválidas.")

        login_timestamp = datetime.datetime.now(datetime.timezone.utc)
        user.last_login = login_timestamp.isoformat().replace('+00:00', 'Z')
        refresh = RefreshToken.for_user(user)

        user.save()
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

    @staticmethod
    def update_user(user_id: int, data:dict):
        try:
            user = User.objects.get(id=user_id)
            for field, value  in data.items():
                if hasattr(user, field):
                    setattr(user, field, value)
            user.save()
            return user
        
        except User.DoesNotExist:
            raise ValidationError("Usuario no encontrado.")
