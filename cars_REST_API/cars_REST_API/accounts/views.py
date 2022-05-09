from rest_framework import generics

# Create your views here.
from rest_framework.views import APIView

from cars_REST_API.accounts.models import ProfileModel
from cars_REST_API.accounts.serializers import ProfileSerializer


class Login(APIView):
    pass
    # serializer_class = UserSerializer()
    #
    #
    # def post(self,request):
    #     serializer =


class Register(APIView):
    pass


class UpdateProfileAPIView(generics.UpdateAPIView):

    serializer_class = ProfileSerializer
    lookup_field = 'id'
    queryset = ProfileModel.objects.all()

