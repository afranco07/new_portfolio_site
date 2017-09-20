from django.shortcuts import render
from django.http import HttpResponse
from portfolio.models import Project, Language
import random

# Create your views here.

def index(request):
    all_projects = Project.objects.all()
    random_projects = []
    for x in range(3):
        number = random.randint(0, len(all_projects) - 1)
        random_projects.append(all_projects[number])

    return render(request, 'portfolio/infoTabs.html', {"randomProjects": random_projects})

def projects(request):
    ios_projects = Project.objects.filter(language__language='iOS')
    java_projects = Project.objects.filter(language__language='Java')
    html_projects = Project.objects.filter(language__language='HTML/CSS')
    python_projects = Project.objects.filter(language__language='Python')
    projects = {
        "iOSProjects": ios_projects,
        "JavaProjects": java_projects,
        "HTML": html_projects,
        "PythonProjects": python_projects,
    }
    return render(request, 'portfolio/projectsPage.html', projects)

def about(request):
    return render(request, 'portfolio/aboutPage.html', {})
