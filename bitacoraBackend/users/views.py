from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
from .services import UserService

class UserViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    @permission_classes([AllowAny])
    def register(self, request):
        data = request.data
        user = UserService.register_user(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        )
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    @permission_classes([AllowAny]) 
    def login(self, request):
        data = request.data
        auth_data = UserService.authenticate_user(
            username=data.get('username'),
            password=data.get('password')
        )
        response = Response(auth_data, status=status.HTTP_200_OK)
        response.set_cookie(
                    key='access_token',
                    value=auth_data["access"],
                    httponly=True,
                    secure=False,
                    samesite='Lax',
                    max_age=60*15  
                )

        return response

    @action(detail=False, methods=['get'])
    @permission_classes([IsAuthenticated])
    def profile(self, request):
        user = request.user
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)