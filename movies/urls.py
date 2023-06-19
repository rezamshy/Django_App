from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesView.as_view(), name = 'movies.list'),
    path('create', views.CreateMovieView.as_view(), name = 'movies.create'),
]