from django.shortcuts import render
from .models import Project, Images, Certificates

# Create your views here.


def index(request):
    projects = Project.objects.all()
    certificates = Certificates.objects.all()

    context = {
        'page_title': "Mishary",
        'projects': projects,
        'Certificates': certificates,
    }
    return render(request, 'index.html', context)


def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'page_title': "project",
        'project': project,
    }
    return render(request, 'projects/project_details.html', context)


def about(request):
    context = {
        'page_title': "about",
    }
    return render(request, 'projects/about.html', context)
