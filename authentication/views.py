from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction
from authentication.serializers import UserSerializer, UserLoginSerializer


class RegistrationView(APIView):
    """
    View for registering a new user to your system.

    **Example requests**:

        POST /api/auth/register/
    """

    @transaction.atomic()
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    View for login a user to your system.

    **Example requests**:

        POST /api/auth/login/
    """

    @transaction.atomic()
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        try:
            user = User.objects.get(username=username)
            authenticated_user = authenticate(username=user.username, password=password)
            serializer = UserLoginSerializer(authenticated_user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)