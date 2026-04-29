from django.db import models

# Create your models here.
class project(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField()
     github_link = models.URLField()

     def _str_(self):
         return self.title
