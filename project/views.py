from django.core.mail import send_mass_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from djoser.views import UserViewSet

from rest_framework.viewsets import ModelViewSet , GenericViewSet
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from djoser.views import UserViewSet as BaseUserViewSet
from django.conf import settings

from . import serializers, models


"""
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ViewModifyProjectSerializer
    permission_classes = [permissions.IsProjectLeaderOrAuthenticatedUser]
    
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return CreateProjectSerializer
        return ViewModifyProjectSerializer

"""
        
class EtablissementViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']
    queryset = models.Etablissement.objects.all()
    serializer_class = serializers.EtablissementSerializer
    
    def get_permissions(self):
        if self.request.method in ['POST','PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]
    
    
class StudentViewSet(ModelViewSet):
    queryset = models.Student.objects.select_related('etablissement').all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [IsAdminUser]
    
    @action(detail=False, methods=['GET', 'PUT', 'PATCH'], permission_classes=[IsAuthenticated])
    def me(self, request):
        student = models.Student.objects.get(
            user_id=request.user.id
        )
        if request.method == 'GET':
            serializer = serializers.StudentSerializer(student)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = serializers.StudentSerializer(student, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = serializers.BaseStudentSerializer(student, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        



    
    
    
        






    
    
    
    