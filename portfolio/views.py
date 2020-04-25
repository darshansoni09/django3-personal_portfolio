from django.shortcuts import render
from .models import Projects

def home(request):

    project = Projects.objects.all()
    return render(request, 'portfolio/home.html', {'project':project})
