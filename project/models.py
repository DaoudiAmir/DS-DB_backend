from django.contrib import admin
from django.conf import settings
from django.db import models



# class Student
# class Professor 
# class Project 


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
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES)
    status = models.CharField(max_length=50, choices=PROJECT_STATUS_CHOICES, default=ON_HOLD)
    deposition_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True , null=True)
    project_leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT) #  a Leader(Professor) can have multiple Projects
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , blank=True , null=True , related_name='supervisor_user')
    co_supervisor = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , blank=True , null=True, related_name='co_supervisor_user')
    trademark_name = models.CharField(max_length=255 , blank=True , null=True)
    scientific_product_name = models.CharField(max_length=255 , blank=True , null=True)
    description = models.TextField()
    # participants : a project can have multiple participants including students and professors 
    # but participants can be in only one project ,but professor can participate in multiple projects 
    
    def __str__(self) -> str:
        return self.title
