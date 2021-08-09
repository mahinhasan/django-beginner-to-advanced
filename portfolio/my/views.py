from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,TemplateView
# Create your views here.


class HomePage(TemplateView):

    template_name = 'my/index.html'