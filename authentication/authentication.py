from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

from helpers.jwt_helper import JWTHelper


class UserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        if 'HTTP_AUTHORIZATION' in request.META:
            token = request.META.get('HTTP_AUTHORIZATION').replace("Bearer ", "")
            if not token:
                raise exceptions.AuthenticationFailed('No token provided')
            is_valid, message = JWTHelper.is_token_valid(token)
            if is_valid:
                username = JWTHelper.decode_token(token)
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    raise exceptions.AuthenticationFailed('No such user')
                return user, None
            raise exceptions.AuthenticationFailed(message)
        raise exceptions.AuthenticationFailed('No token provided')