from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=50)

class Feature(models.Model):
    date = models.DateTimeField()
    description = models.CharField(max_length=200)
    lead_developer = models.ForeignKey(Developer)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

class Customer(models.Model):
    name = models.CharField(max_length=50)
    last_viewed_feature = models.DateTimeField()
