from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

AUTH_COOKIE_NAME = getattr(settings, 'AUTH_COOKIE_NAME', 'access_token')

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        raw_token = request.COOKIES.get(AUTH_COOKIE_NAME)
        if raw_token is None:
            return None
        try:
            validated = self.get_validated_token(raw_token)
            user = self.get_user(validated)
            return (user, validated)
        except InvalidToken:
            return None