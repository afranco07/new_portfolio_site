from django.shortcuts import render
from django.http import HttpResponse
from portfolio.models import Project, Language

# Create your views here.

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'portfolio/infoTabs.html', context=context_dict)

def projects(request):
    data = Project.objects.filter(language__language='iOS')
    return render(request, 'portfolio/iOSProjects.html', {"data": data})

def about(request):
    return render(request, 'portfolio/aboutPage.html', {})
