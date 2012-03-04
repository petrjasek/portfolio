from django.views.generic import ListView, DetailView
from models import *

class IndexView(ListView):
    context_object_name = "project_list"
    template_name = "index.html"
    queryset = Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['current'] = 'index'
        return context

class ProjectView(DetailView):
    context_object_name = "project"
    template_name = "project.html"
    model = Project

