from rest_framework import serializers


class LoginSerialzer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
