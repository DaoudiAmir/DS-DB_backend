from django.core.mail import send_mass_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from djoser.views import UserViewSet
from . import serializers
from rest_framework.viewsets import ModelViewSet , GenericViewSet
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from .models import Student, Teacher

# add emails here


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer 
    permission_classes = [IsAdminUser]
    
    @action(detail=False, methods=['GET', 'PUT'], permission_classes= [IsAuthenticated])
    def me(self, request):
        student = Student.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = serializers.StudentSerializer(student)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = serializers.StudentSerializer(student, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    
    
    
    