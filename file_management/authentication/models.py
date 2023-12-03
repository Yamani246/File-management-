from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from .manager import CustomUserManager

class AcademicYear(models.Model):
    year=models.CharField(max_length=50, unique=True ,default='')
    def __str__(self):
        return self.year
    
class Department(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, default='')
    email = models.EmailField(unique=True, default='')
    name=models.CharField(max_length=100,default='')
    uni_id = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, null=True, blank=True)
    sections=models.CharField(max_length=50,default='',null=True,blank=True)
    department=models.ForeignKey(Department, on_delete=models.CASCADE,null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'  

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class File(models.Model):
    file = models.FileField(upload_to='media/')
    upload_date = models.DateTimeField(default=timezone.now)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    file_name=models.CharField(max_length=256,default='')
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear,on_delete=models.CASCADE)