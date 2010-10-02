from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
  url = models.URLField()

class Bookmark(models.Model):
  title = models.CharField(max_length=200)
  user = models.ForeignKey(User)
  link = models.ForeignKey(Link)
class Tag(models.Model):
  name = models.CharField(max_length=64, unique=True)
  bookmarks = models.ManyToManyField(Bookmark)

