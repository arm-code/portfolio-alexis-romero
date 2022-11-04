from django.shortcuts import render

from files_manager.models import Drawing

# Create your views here.

def files_manager(request):
    drawings = Drawing.objects.all()
    return render(request, 'welcome_files.html', {'drawings': drawings})

def login_files_manager(request):
    return render(request, 'login.html', {})