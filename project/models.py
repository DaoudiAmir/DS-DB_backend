from django.contrib import admin
from django.conf import settings
from django.db import models
from django.utils.html import mark_safe

class Etablissement(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    
    def __str__(self) -> str:
         return self.name


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, blank=True, null=True)
    num_inscription = models.BigIntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='project/images', null=True, blank=True)
    filiére = models.CharField(max_length=255, null=True, blank=True)
    spécialité = models.CharField(max_length=100, null=True, blank=True)
    
    def profile_picture_preview(self): #new
            return mark_safe(f'<img src = "{self.profile_picture.url}" width="100px" height= "100px" object-fit="cover"/>')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
     
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name'] 





"""
class Project (models.Model):
    
    ACTIVE = 'Active'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'
    ON_HOLD = 'On Hold'
    REJECTED = 'Rejected'
    
    PROJECT_STATUS_CHOICES = [
    (ACTIVE,'Active'),
    (COMPLETED,'Completed'),
    (CANCELLED,'Cancelled'),
    (ON_HOLD,'On Hold'),
    (REJECTED,'Rejected'),
]


    STARTUP = 'un diplôme - une startup'
    PATENT = 'Un diplôme - Un Brevet'

    PROJECT_TYPE_CHOICES = [
        (STARTUP,'un diplôme - une startup'),
        (PATENT,'Un diplôme - Un Brevet')
    ]
    
    title = models.CharField(max_length=255)
    establishment = models.CharField(max_length=255)
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES, help_text=_('Select the type of the project'),)
    status = models.CharField(max_length=50, choices=PROJECT_STATUS_CHOICES, default=ON_HOLD)
    deposition_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True , null=True)
    project_leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT) #  a Leader(Professor) can have multiple Projects
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , blank=True , null=True , related_name='supervisor_user')
    co_supervisor = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , blank=True , null=True, related_name='co_supervisor_user')
    trademark_name = models.CharField(max_length=255 , blank=True , null=True, help_text=_('Enter this if the project type is "un diplôme - une startup"'),)
    scientific_product_name = models.CharField(max_length=255 , blank=True , null=True, help_text=_('Enter this if the project type is "un diplôme - un Brevet"'),)
    description = models.TextField()
    participant = models.ManyToManyField(User, blank=True , related_name='participants')
    
    # participants : a project can have multiple participants including students and professors 
    # but participants can be in only one project ,but professor can participate in multiple projects 
    
    def __str__(self) -> str:
        return self.title
"""   
