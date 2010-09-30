from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
  url = models.URLField()

class Bookmark(models.Model):
  title = models.CharField(maxlength=200)
  user = models.ForeignKey(User)
  link = models.ForeignKey(Link)

