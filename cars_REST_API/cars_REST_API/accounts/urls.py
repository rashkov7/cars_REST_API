from django.urls import path

from cars_REST_API.accounts.views import UpdateProfileAPIView, Login, Register

urlpatterns = (
    path('<int:id>', UpdateProfileAPIView.as_view(), name='profile'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
)
