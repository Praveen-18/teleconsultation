from django.db import models

# Create your models here.


class farmerDetails(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    user_name = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.user_name


class consultantDetails(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    user_name = models.CharField(max_length=30, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    speciality = models.CharField(max_length=30)
    qualification = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.user_name