from django.urls import path, include
from . import views

urlpatterns = [    
    path('', views.files_manager, name='files_manager')
]