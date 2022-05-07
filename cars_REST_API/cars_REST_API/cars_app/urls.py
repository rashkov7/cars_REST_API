from django.urls import path

from cars_REST_API.cars_app.views import CarBrandCreateListAPIView,\
    CarBrandDetailsAPIView,CarModelLIstCreateAPIView, CarModelUpdateDeleteAPIView

urlpatterns = (
    path('brand/', CarBrandCreateListAPIView.as_view()),
    path('brand/<int:id>', CarBrandDetailsAPIView.as_view()),
    path('models/', CarModelLIstCreateAPIView.as_view()),
    path('models/<int:id>', CarModelUpdateDeleteAPIView.as_view()),
)
