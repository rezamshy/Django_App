from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MoviesView(TemplateView):
    template_name = 'movies.html'
    extra_context = {'movies': 'https://www.omdbapi.com/src/poster.jpg'}