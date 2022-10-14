from django.shortcuts import render

# Create your views here.

def files_manager(request):
    return render(request, 'welcome_files.html', {})