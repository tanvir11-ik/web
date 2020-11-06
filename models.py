from django.db import models

# Create your models here.

class admin(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    bdate = models.TextField()
    disc = models.TextField()
    mobile = models.IntegerField()
