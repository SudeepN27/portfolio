from django.shortcuts import render
from .models import project

def home(request):
    return render(request, 'home.html')

def projects(request):
    projects = project.objects.all()   # ✅ this returns list (QuerySet)
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

# Create your views here.
