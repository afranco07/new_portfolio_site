from django.shortcuts import render
from django.http import HttpResponse
from portfolio.models import Project, Language

# Create your views here.

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'portfolio/infoTabs.html', context=context_dict)

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
