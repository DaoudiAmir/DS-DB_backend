from django.contrib import admin
from django.utils.html import mark_safe
from django.conf import settings
from django.contrib.auth.models import  AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
   is_student = models.BooleanField(_('student'),
                                    default=False,
                                    help_text=_('Designates whether the user is a student'), unique=True)
   is_teacher = models.BooleanField(_('teacher'),
                                    default=False,
                                    help_text=_('Designates whether the user is a teacher'), unique=True)    
           
   email = models.EmailField(unique=True)
   
   REQUIRED_FIELDS = ['email', 'is_student', 'is_teacher']
   
   
   
   
   
class Teacher(models.Model):
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    registration_number = models.IntegerField()
    birth_date = models.DateField()
    phone = models.CharField(max_length=255)
    establishment = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='core/images')
    grade = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
     
    def __str__(self) -> str:
        return self.user.username
   


class Student(models.Model):
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    registration_number = models.IntegerField()
    birth_date = models.DateField()
    phone = models.CharField(max_length=255)
    establishment = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='core/images') 
    sector = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.user.username
    
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    def picture_preview(self): #new
        return mark_safe(f'<img src = "{self.picture.url}" width="100px" height= "100px" object-fit="cover"/>')
    class Meta:
        ordering = ['registration_number',]
    

        
        


   
