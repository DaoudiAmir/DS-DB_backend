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
        



class TeacherViewSet(ModelViewSet):
    queryset = models.Teacher.objects.select_related('etablissement').all()
    serializer_class = serializers.TeacherSerializer
    permission_classes = [IsAdminUser]
    
    @action(detail=False, methods=['GET', 'PUT', 'PATCH'], permission_classes=[IsAuthenticated])
    def me(self, request):
        teacher = models.Teacher.objects.get(
            user_id=request.user.id
        )
        if request.method == 'GET':
            serializer = serializers.TeacherSerializer(teacher)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = serializers.TeacherSerializer(teacher, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = serializers.BaseTeacherSerializer(teacher, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    
    
######## Project Deposition


class PeriodViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options'] 
    queryset = models.Period.objects.all()  
    serializer_class = serializers.PeriodSerializer
    
    
class ProjectInvitationViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options'] 
    queryset = models.ProjectInvitation.objects.all()
    serializer_class = serializers.ProjectInvitationSerializer
    
    
class ProjectTeamViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options'] 
    queryset = models.ProjectTeam.objects.all()
    serializer_class = serializers.ProjectTeamSerializer
    
    
class ManagementTeamViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options'] 
    queryset = models.ManagementTeam.objects.all()
    serializer_class = serializers.ManagementTeamSerializer
    
class ProjectTypeViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options'] 
    queryset = models.ProjectType.objects.all()
    serializer_class = serializers.ProjectTypeSerializer
    
    
class ProjectViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options'] 
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    
    
######## Project Validation


class ValidationCommitteeViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options'] 
    queryset = models.ValidationCommittee.objects.all()
    serializer_class = serializers.ValidationCommitteeSerializer
    
class DecisionOfCommitteeViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options'] 
    queryset = models.DecisionOfCommittee.objects.all()
    serializer_class = serializers.DecisionOfCommitteeSerializer
    
    
class ProjectValidationViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options'] 
    queryset = models.ProjectValidation.objects.all()
    serializer_class = serializers.ProjectValidationSerializer
    

#### gestion recours

class RecoursViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options'] 
    queryset = models.Recours.objects.all()
    serializer_class = serializers.RecoursSerializer


class RecoursValidationViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options'] 
    queryset = models.RecoursValidation.objects.all()
    serializer_class = serializers.RecoursValidationSerializer    
        
            






    
    
    
    