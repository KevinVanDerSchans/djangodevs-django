from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional e-commerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None

    for i in projectsList:
        if i['id'] == pk:
            projectObj = i

    return render(request, 'projects/single-project.html', {'project': projectObj})
