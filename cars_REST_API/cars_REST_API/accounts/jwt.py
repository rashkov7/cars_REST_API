from django.contrib.auth import get_user_model

from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header, BaseAuthentication
import jwt
from django.conf import settings

UserModel = get_user_model()


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_headers = get_authorization_header(request)
        auth_data = auth_headers.decode('utf-8')
        auth_token = auth_data.split(" ")

        if len(auth_token) == 2:
            token = auth_token[1]
            try:
                payload =jwt.decode(token,settings.SECRET_KEY, algorithms="HS256")
                email = payload['email']
                user = UserModel.objects.get(email=email)
                return user, token

            except jwt.ExpiredSignatureError as ex:
                raise exceptions.AuthenticationFailed('Token is expired')

            except jwt.DecodeError as ex:
                raise exceptions.AuthenticationFailed('Token is invalid')

        raise exceptions.AuthenticationFailed("Token not valid")
