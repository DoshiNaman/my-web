from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    project=models.CharField(max_length=122)
    msg=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Work(models.Model):
    title=models.CharField(max_length=122)
    link=models.CharField(max_length=255)
    desc=models.CharField(max_length=1000)
    date=models.DateField()
    image=models.ImageField(upload_to="work/image",default="")

    def __str__(self):
        return self.title

class Info(models.Model):
    name=models.CharField(max_length=255,default="")
    title=models.CharField(max_length=255,default="")
    phone=models.CharField(max_length=255,default="")
    email=models.EmailField(max_length=255,default="")
    location=models.CharField(max_length=255,default="")
    home_desc=models.TextField(default="")
    about_desc=models.TextField(default="")
    year_experience=models.IntegerField(default=0)
    completed_project=models.IntegerField(default=0)
    companies_worked=models.IntegerField(default=0)        
    
    def __str__(self):
        return self.name

class Education(models.Model):
    title=models.CharField(max_length=255,default="")
    univercity=models.CharField(max_length=255,default="")
    start_year=models.CharField(max_length=12,default="")
    end_year=models.CharField(max_length=12,default="")

    def __str__(self):
        return self.title
    
class Job(models.Model):
    title=models.CharField(max_length=255,default="")
    company=models.CharField(max_length=255,default="")
    start_year=models.CharField(max_length=12,default="")
    end_year=models.CharField(max_length=12,default="")
    
    def __str__(self):
        return self.title

class Achievement(models.Model):
    title=models.CharField(max_length=255,default="")
    achiev=models.CharField(max_length=255,default="")
    achiev_year=models.IntegerField(default=2002)
    
    def __str__(self):
        return self.title

class Services(models.Model):
    title=models.CharField(max_length=255,default="")
    icon=models.CharField(max_length=255,default="")
    ser1=models.CharField(max_length=255,default="")
    ser2=models.CharField(max_length=255,default="")
    ser3=models.CharField(max_length=255,default="")
    ser4=models.CharField(max_length=255,default="")   

    def __str__(self):
        return self.title         

class Social(models.Model):
    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    def __str__(self):
        return self.title


    