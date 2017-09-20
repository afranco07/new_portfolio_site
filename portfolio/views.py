from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'portfolio/infoTabs.html', context=context_dict)

def projects(request):
    return render(request, 'portfolio/iOSProjects.html', {})

def about(request):
    return render(request, 'portfolio/aboutPage.html', {})
