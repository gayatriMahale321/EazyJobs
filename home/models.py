from operator import truediv
# from click import password_option
from django.db import models

# Create your models here.
class contactus(models.Model):
    email=models.CharField(max_length=100)
    mob=models.CharField(max_length=12)
    msg=models.CharField(max_length=150)
    
class Student(models.Model):
    sname= models.CharField(max_length=40)
    mobile=models.CharField(max_length=10)
    sadd=models.TextField(max_length=200)
    city=models.CharField(max_length=30)
    pincode=models.CharField(max_length=6)
    email=models.EmailField(max_length=200)
    domainknowledge=models.CharField(max_length=100)
    workexpinyears=models.IntegerField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=100)

class Company(models.Model):
    cregno=models.CharField(max_length=15,primary_key=True)
    cname= models.CharField(max_length=40)
    cindustry=models.CharField(max_length=40)
    Phone=models.CharField(max_length=10)
    cadd=models.TextField(max_length=200)
    city=models.CharField(max_length=30)
    pincode=models.CharField(max_length=6)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=100)
    
class JobOpening(models.Model):
    cregno=models.CharField(max_length=15)
    openingfor=models.CharField(max_length=30)
    forfresher=models.CharField(max_length=5)
    expinyear=models.IntegerField()
    joblocation=models.CharField(max_length=100)
    ctc=models.CharField(max_length=10)
    details=models.TextField()




