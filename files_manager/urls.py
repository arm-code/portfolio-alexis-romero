from django.urls import path, include
from . import views

urlpatterns = [    
    path('files-manager', views.files_manager, name='files_manager'),
    path('login',views.login_files_manager, name='login_files_manager'),
]