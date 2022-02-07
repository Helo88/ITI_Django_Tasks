from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    


class Students(models.Model):
    id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    email= models.CharField(max_length=20)
    password= models.CharField(max_length=20)
    confirm_password= models.CharField(max_length=20,default=None)
    
    def __str__(self):
        return (f" {self.name} {self.name} {self.email}")
        


###################day3 

class Intake(models.Model):
    id=models.AutoField(primary_key=True)
    number=models.IntegerField(null=False)
    name=models.CharField(max_length=30,null=False,blank=False)
    start_date=models.DateField(null=False)
    end_date=models.DateField(null=False)
    students=models.ManyToManyField(Students)
    manager=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return (f"{self.name} {self.number}")
