from django.contrib.auth.models import  AbstractUser
from django.db import models

class User(AbstractUser):
   email = models.EmailField(unique=True)
   birth_date = models.DateField()
   
   
   REQUIRED_FIELDS = ['email', 'birth_date']
