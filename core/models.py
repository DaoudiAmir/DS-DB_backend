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
                                    help_text=_('Designates whether the user is a student'),)
   is_teacher = models.BooleanField(_('teacher'),
                                    default=False,
                                    help_text=_('Designates whether the user is a teacher'),)   
   is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    ) 
           
   email = models.EmailField(unique=True)
   birth_date = models.DateField(blank=True, null=True)
   phone = models.CharField(max_length=255, blank=True, null=True)
   registration_number = models.BigIntegerField(unique=True)
   establishment = models.CharField(max_length=255, blank=True, null=True)
   specialty = models.CharField(max_length=255, blank=True, null=True)
   grade = models.CharField(max_length=255,
                            help_text=_('Designates the grade of the teacher'),
                            blank=True, null=True) #teacher
   sector = models.CharField(max_length=255,
                             help_text=_('Designates the sector of the student'),
                             blank=True, null=True) #student
   
   picture = models.ImageField(upload_to='core/images',
                               help_text=_('Define your profile picture'),
                               blank=True, null=True)
   
   

    
   
   REQUIRED_FIELDS = ['email', 'is_student', 'is_active', 'is_teacher', 'registration_number']
   
   def picture_preview(self): #new
        return mark_safe(f'<img src = "{self.picture.url}" width="100px" height= "100px" object-fit="cover"/>')
     
     


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
    participant = models.ManyToManyField(User, blank=True , related_name='participants')
    
    # participants : a project can have multiple participants including students and professors 
    # but participants can be in only one project ,but professor can participate in multiple projects 
    
    def __str__(self) -> str:
        return self.title
   