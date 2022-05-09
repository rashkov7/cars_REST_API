from django.urls import path

from cars_REST_API.cars_app.views import CarBrandCreateListAPIView, \
    CarBrandDetailsAPIView, CarModelLIstCreateAPIView, CarModelUpdateDeleteAPIView, CarUserListCreateAPIView, \
    CarUserUpdateDeleteAPIView

urlpatterns = (
    path('brands/', CarBrandCreateListAPIView.as_view(), name='all brands'),
    path('brands/<int:id>', CarBrandDetailsAPIView.as_view(), name='brand'),
    path('models/', CarModelLIstCreateAPIView.as_view(), name='all models'),
    path('models/<int:id>', CarModelUpdateDeleteAPIView.as_view(), name='model'),
    path('usercar/', CarUserListCreateAPIView.as_view(), name='model'),
    path('usercar/<int:id>', CarUserUpdateDeleteAPIView.as_view(), name='model'),
)
