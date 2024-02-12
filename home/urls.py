from django.urls import path
from .views import PersonView

app_name = "home"
urlpatterns = [
    path('', PersonView.as_view(), name="person"),
]