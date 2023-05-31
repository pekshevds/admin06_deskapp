from django.shortcuts import render, redirect
from app.models import Project, Document
from app.fetchers import get_object_or_none


def index(request):
    projects = Project.objects.all()
    project = None
    documents = None

    context = {
        'projects': projects,
        'project': project,
        'documents': documents
        }
    return render(request=request, template_name='app/index.html', context=context)


def project_new(request):

    if request.method == "POST":
        return redirect('show-index-page')

    projects = Project.objects.all()
    project = None
    documents = None

    context = {
        'projects': projects,
        'project': project,
        'documents': documents
        }
    return render(request=request, template_name='app/form-new-project.html', context=context)


def project_edit(request, project_id=''):

    if request.method == "POST":
        return redirect('show-index-page')

    projects = Project.objects.all()
    project = get_object_or_none(Class=Project, pk=project_id)
    documents = None

    context = {
        'projects': projects,
        'project': project,
        'documents': documents
        }
    return render(request=request, template_name='app/form-project.html', context=context)


def document_new(request):

    if request.method == "POST":
        return redirect('show-index-page')

    projects = Project.objects.all()
    project = None

    context = {
        'projects': projects,
        'project': project
        }
    return render(request=request, template_name='app/form-new-document.html', context=context)


def document_edit(request, document_id=''):

    if request.method == "POST":
        return redirect('show-index-page')

    projects = Project.objects.all()
    project = None
    document = get_object_or_none(Class=Document, pk=document_id)

    context = {
        'projects': projects,
        'project': project,
        'documents': document
        }
    return render(request=request, template_name='app/form-document.html', context=context)


def project_content(request, project_id=''):
    projects = Project.objects.all()
    project = get_object_or_none(Class=Project, pk=project_id)
    documents = Document.objects.filter(project=project)

    context = {
        'projects': projects,
        'project': project,
        'documents': documents
        }
    return render(request=request, template_name='app/index.html', context=context)
