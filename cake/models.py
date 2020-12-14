from django.db import models

# Create your models here.
class Cake(models.Model):

    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to ='pics')
    quantity = models.CharField(max_length=50,default=' ')

class Special(models.Model):

    name = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to ='pics')