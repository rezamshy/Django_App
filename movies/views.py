from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import Movie

# Create your views here.

class CreateMovieView(CreateView):
    template_name = "movies/create_movie.html"
    model = Movie
    fields = ["title", "poster_url", "rate"]
    success_url = '/movies'


class MoviesView(ListView):
    template_name = 'movies/movies.html'
    model = Movie
    context_object_name = 'movies'