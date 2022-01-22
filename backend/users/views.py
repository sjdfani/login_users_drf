from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .utils import get_token_user
from .serializer import LoginSerialzer


class LoginUser(APIView):
    # authentication_classes = []

    def post(self, request):
        msg = dict()
        serializer = LoginSerialzer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data['email']
            password = serializer.data['password']
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                msg['message'] = f"{email} is not exist."
                return Response(msg, status=status.HTTP_404_NOT_FOUND)
            if user.check_password(password):
                tokens = get_token_user(user)
                return Response(tokens, status=status.HTTP_200_OK)
            else:
                msg['message'] = "Your password is incorrect."
                return Response(msg, status=status.HTTP_404_NOT_FOUND)