from django.urls import path
from .views import index, AddTask, EditTask, DeleteTask
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('add/', AddTask.as_view(), name='add'),
    path('<int:pk>/edit/', EditTask.as_view(), name='edit'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='delete'),
]