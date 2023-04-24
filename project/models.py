from django.contrib import admin
from django.conf import settings
from django.db import models



# class Student
# class Professor 
# class Project 

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
    
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=PROJECT_STATUS_CHOICES, default=ON_HOLD)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    supervisors = models.ManyToManyField(Professor, related_name='supervisors') # the supervisors (les encadrants)
    project_leader = models.ForeignKey(Professor, on_delete=models.PROTECT) #  a Leader(Professor) can have multiple Projects
    # participants : a project can have multiple participants including students and professors 
    # but participants can be in only one project ,but professor can participate in multiple projects 
    
    def __str__(self) -> str:
        return self.title"""