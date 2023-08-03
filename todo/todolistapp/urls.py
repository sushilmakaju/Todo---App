from .views import *
from django.urls import path

urlpatterns = [
    path('home/', home, name='home'),
    path('create/', create_todo, name= 'create'),
    path('edit/<pk>/', edit, name='edit'),
    path('delete/<pk>/', delete, name = 'delete')
]
