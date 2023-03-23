from django.contrib import admin
from django.conf import settings
from django.db import models



# class Student
# class Professor 
# class Project 

class Professor (models.Model):
    
    phone = models.CharField(max_length=50)
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     
    def __str__(self) -> str:
        return self.user.first_name
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    def email(self):
        return self.user.email
    
    def birth_date(self):
        return self.user.birth_date

    class Meta:
        ordering = ['user__first_name', 'user__last_name']


class Student (models.Model):
    
    registration_number = models.IntegerField()
    supervisor = models.ForeignKey(Professor, on_delete=models.PROTECT,) 
    project = models.ForeignKey('Project', on_delete=models.PROTECT)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     
    def __str__(self) -> str:
        return self.user.first_name
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    def email(self):
        return self.user.email
    
    def birth_date(self):
        return self.user.birth_date

    class Meta:
        ordering = ['user__first_name', 'user__last_name']



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
        return self.title