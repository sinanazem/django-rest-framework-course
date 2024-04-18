from django.urls import path, include
from .views import UserRegister
from rest_framework.authtoken import views as authtoken_views

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegister.as_view()),
]


urlpatterns += [
    path('api-token-auth/', authtoken_views.obtain_auth_token)
]