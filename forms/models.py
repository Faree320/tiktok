from django.db import models

# Create your models here.


# class GetLink(models.Model):
#     link1 = models.CharField(max_length=400)
#     link2 = models.CharField(max_length=400)
#     link3 = models.CharField(max_length=400)
#


class KeySearch(models.Model):
    genre = models.CharField(max_length=10_000, null=True, blank=True)
