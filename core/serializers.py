from django.contrib.auth import authenticate, get_user_model
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from requests import request
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer as BaseTokenObtainSerializer, TokenObtainPairSerializer as BaseTokenObtainPairSerializer

from dsdb.settings import MEDIA_URL
from . import models


from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import update_last_login
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError

from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken, UntypedToken

from djoser.serializers import UserSerializer as BaseUserSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

from core.models import User


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['is_student', 'is_teacher', 'username', 'password',
                  'email', 'first_name', 'last_name', 'registration_number',
                  'phone', 'establishment', 'specialty', 'grade',
                  'sector', 'picture'] 
        


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['is_student', 'is_teacher', 'registration_number', 'username', 
                  'first_name', 'last_name', 'phone', 'establishment',
                  'specialty', 'sector', 'grade', 'picture']
    
        


class ViewModifyProjectSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only= True)
    project_type = serializers.CharField(read_only= True)
    project_leader = serializers.StringRelatedField()
    supervisor = serializers.StringRelatedField()
    co_supervisor = serializers.StringRelatedField()
    participant = serializers.StringRelatedField( many=True)
    class Meta:
        model = models.Project
        fields = ['id','title','establishment','project_type','status',
                  'project_leader','supervisor',
                  'co_supervisor','trademark_name','scientific_product_name',
                  'description', 'participant']
        depth = 1

class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Project
        fields = '__all__'

    
        
    
    

    
      