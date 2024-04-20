from django.urls import path, include
from .views import UserRegister, UserViewset
from rest_framework.authtoken import views as authtoken_views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# urlpatterns += [
#     path('api-token-auth/', authtoken_views.obtain_auth_token)
# ]


router = routers.SimpleRouter()
router.register('user', UserViewset)
urlpatterns += router.urls

