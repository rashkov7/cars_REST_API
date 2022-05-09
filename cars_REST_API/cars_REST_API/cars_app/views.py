from rest_framework import response, status
from rest_framework.views import APIView
from rest_framework import generics

from cars_REST_API.cars_app.models import CarBrand, CarModel, UserCar
from cars_REST_API.cars_app.serializers import CarBrandSerializer, CarModelSerializer, UserCarSerializer


class CarBrandCreateListAPIView(APIView):
    serializer_class = CarBrandSerializer

    def get(self, request):
        car_brands = CarBrand.objects.all()
        serializer = self.serializer_class(car_brands, many=True)
        return response.Response({"car brands": serializer.data})

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"Car Brand": serializer.data}, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarBrandDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CarBrandSerializer
    lookup_field = 'id'
    queryset = CarBrand.objects.all()


class CarModelLIstCreateAPIView(generics.ListCreateAPIView):

    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()


class CarModelUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CarModelSerializer
    lookup_field = 'id'
    queryset = CarModel.objects.all()


class CarUserListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = UserCarSerializer
    queryset = UserCar.objects.all()


class CarUserUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = UserCarSerializer
    lookup_field = 'id'
    queryset = UserCar.objects.all()

