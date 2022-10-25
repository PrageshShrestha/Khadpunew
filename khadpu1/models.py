from django.db import models
class Images(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=10000)
    image = models.ImageField(upload_to = 'static/')
    description = models.CharField(max_length = 5000)
    location = models.CharField(max_length = 10900)
    type= models.CharField(max_length = 290)

class Gallery(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to = 'static/')
    name = models.CharField(max_length = 500)
class Politics(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to = 'static/') 
    name = models.CharField(max_length = 1000)
    position = models.CharField(max_length = 500)
    about_khadpu = models.CharField(max_length = 10000)   
    facebook = models.CharField(max_length = 10000)
        
# Create your models here.
