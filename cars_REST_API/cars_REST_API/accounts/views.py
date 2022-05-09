import logging

from django.contrib.auth import authenticate, get_user_model
from rest_framework import generics, status

from rest_framework import response
from rest_framework.views import APIView

from cars_REST_API.accounts.models import ProfileModel
from cars_REST_API.accounts.serializers import ProfileSerializer, UserSerializer, LoginSerializer

UserModel = get_user_model()


class Login(APIView):
    authentication_classes = ()
    serializer_class = LoginSerializer

    def get(self, request):
        return response.Response()

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)
            return response.Response({"user": serializer.data})
        return response.Response({"message": "invalid credentials,try again!"}, status=status.HTTP_400_BAD_REQUEST)


class Register(APIView):
    serializer_class = UserSerializer
    authentication_classes = ()

    def get(self, request):
        return response.Response()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"user": serializer.data})
        return response.Response(serializer.errors)


class UpdateProfileAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    queryset = ProfileModel.objects.all()
