from django.db import models
# Create your models here.
class Student(models.Model):
    id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    email= models.CharField(max_length=20)
    

class Students(models.Model):
    id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    email= models.CharField(max_length=20)
    password= models.CharField(max_length=20)