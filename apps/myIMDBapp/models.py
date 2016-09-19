from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MovieManager(models.Manager):
    def addMovie(self,title,year):
        Movies.movieManager.create(title=title, year=year)
        Movies.movieManager.save()
        return True
    def removeMovie(self,movie_id):
        return False

class ActorManager():
    def addActor(self, first_name, last_name):
        return False
    
class Movies(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    movieManager = MovieManager()

class Actors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    actorManager = ActorManager()
    
class Casts(models.Model):
    FK_actor = models.ForeignKey(Actors)
    FK_movie = models.ForeignKey(Movies)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)