from django.urls import path
from .views import PersonView

urlpatterns = [
    path('', PersonView.as_view(), name="accounts"),
]