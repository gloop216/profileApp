from django.db import models

# Create your models here.
class Project(models.Model):

    name =models.CharField(max_length=100)
    imgTitl=models.ImageField( upload_to='projectPhoto')
    imgDetalone=models.ImageField( upload_to='projectPhoto')
    imgDetalTwo=models.ImageField( upload_to='projectPhoto')
    imgDetalThree=models.ImageField( upload_to='projectPhoto')
    description=models.TextField(max_length=1000)
    date=models.DateField()
    Categroy=models.CharField(max_length=100)
    url=models.URLField(max_length=1000)
    slug=models.SlugField()


class Connect(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=1000)
    msg=models.TextField(max_length=2000)
    
