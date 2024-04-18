from django.urls import path, include
from .views import UserRegister

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegister.as_view()),
]
