from django.shortcuts import render
from django.views.generic import ListView
from app.models import Project


class ProjectListView(ListView):
    template_name = ""
    model = Project


def index(request):
    return render(request=request, template_name='app/index.html')
