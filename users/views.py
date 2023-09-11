from django.contrib import auth
from django.contrib.auth.models import User, update_last_login
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        auth.login(request, user)
        return Response({"msg": "Login successfully"}, status=status.HTTP_200_OK)


class LogoutView(APIView):

    def post(self, request, *args, **kwargs):
        auth.logout(request)
        return Response({"msg": "Logout successfully"}, status=status.HTTP_200_OK)
