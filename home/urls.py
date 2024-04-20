from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('questions/', views.QuestionListView.as_view(), name='question_list_view'),
    path('question/create/', views.QuestionCreateView.as_view(), name='question_create_view'),
    path('question/update/<int:pk>/', views.QuestionUpdateView.as_view(), name='question_update_view'),
    path('question/delete/<int:pk>/', views.QuestionDeleteView.as_view(), name='question_delete_view'),
]
