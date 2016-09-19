from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movies, Actors, Casts

# Create your views here.
def index(request):
    context = {}
    allMovies = Movies.movieManager.all()
    return render(request, 'myIMDB/index.html', context)

def addmovie(request):
    if request.method == 'POST':
        title = request.POST['title']
        year = reqyest.POST['YEAR']
        try:
            Movies.movieManager.addMovie(title,year)
        except:
            return redirect('/')
    return redirect('/')