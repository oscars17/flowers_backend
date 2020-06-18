from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (permissions,
                            status
                            )
from . import serializers


class SignUpAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        serializer = serializers.SignUpSerializer(data)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.data
        return Response(status=status.HTTP_200_OK, data=serializer_data)


class SignInAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        user = authenticate(
            data
        )
        if user:
            return login(request, user)
        else:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
