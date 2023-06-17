from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'
    extra_context = {'movies': 'https://www.omdbapi.com/src/poster.jpg'}