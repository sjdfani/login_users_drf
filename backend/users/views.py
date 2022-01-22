from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .utils import get_token_user


class LoginUser(APIView):
    authentication_classes = []

    def post(self, request):
        msg = dict()
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomUser.objects.get(email=email)
        if user is not None:
            if user.check_password(password):
                tokens = get_token_user(user)
                return Response(tokens, status=status.HTTP_200_OK)
            else:
                msg['message'] = "Your password is incorrect."
                return Response(msg, status=status.HTTP_404_NOT_FOUND)
        else:
            msg['message'] = f"{email} is not exist."
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
