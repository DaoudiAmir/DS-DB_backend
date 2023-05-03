from rest_framework import serializers

from . import models

"""
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
"""

class EtablissementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Etablissement
        fields = ['id', 'logo', 'name', 'description']


class StudentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    
    
    class Meta:
        model = models.Student
        fields = ['id', 'user_id','établissement', 'num_inscription',
                  'birth_date', 'phone_number', 'profile_picture',
                  'filiére', 'spécialité']
        
class BaseStudentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.Student
        fields = ['id', 'user_id', 'num_inscription',
                  'birth_date', 'phone_number', 'profile_picture',
                  'filiére', 'spécialité'] 





class TeacherSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    
    
    class Meta:
        model = models.Teacher
        fields = ['id', 'user_id','etablissement', 'num_inscription',
                  'birth_date', 'phone_number', 'profile_picture',
                  'grade', 'spécialité']
        
class BaseTeacherSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.Teacher
        fields = ['id', 'user_id', 'num_inscription',
                  'birth_date', 'phone_number', 'profile_picture',
                  'grade', 'spécialité'] 
        
        
########### project deposition


class PeriodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Period
        fields = ['id', 'name', 'date_début', 'date_fin']
        
        
class ProjectInvitationSerializer(serializers.ModelSerializer):
    #### this api is responsible of sending emails to users (invitations)
    class Meta:
        model = models.ProjectInvitation
        fields = ['id', 'name' , 'description', 'email'] 
                        
class ProjectTeamSerializer(serializers.ModelSerializer):
    team_leader = serializers.StringRelatedField()
    
   
     ### must include select related 'Student'
    
    class Meta:
        model = models.ProjectTeam
        fields = ['name', 'team_leader', 'members', 'participants']
        
        
class ManagementTeamSerializer(serializers.ModelSerializer):
    superviseur = serializers.StringRelatedField()
    co_superviseur = serializers.StringRelatedField()
    
    class Meta:
        model = models.ManagementTeam
        fields = ['name', 'superviseur', 'co_superviseur']
        
class ProjectTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.ProjectType
        fields = ['id', 'type', 'intitulé_idée_innovante']
        
        
        
        ############## the big boy
class ProjectSerializer(serializers.ModelSerializer):
    project_type = serializers.StringRelatedField()
    établissement = serializers.StringRelatedField()
    period = serializers.StringRelatedField()
    porteur_student = serializers.StringRelatedField()
    porteur_teacher = serializers.StringRelatedField()
    project_team = serializers.StringRelatedField()
    équipe_encadrement = serializers.StringRelatedField()
    
    class Meta:
        model = models.Project
        fields = ['id', 'project_type', 'établissement', 'status', 
                  'period', 'deposition_date', 'porteur_student', 
                  'porteur_teacher', 'project_team', 'équipe_encadrement',
                  'résumé']      
        
        
        
########## Project Validation 

class ValidationCommitteeSerializer(serializers.ModelSerializer):
    établissement = serializers.StringRelatedField()
    
    class Meta:
        model = models.ValidationCommittee
        fields = ['id', 'description', 'établissement', 'members']    
        
        
class DecisionOfCommitteeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.DecisionOfCommittee
        fields = ['id', 'title', 'description']    
        
        
class ProjectValidationSerializer(serializers.ModelSerializer):
    committee = serializers.StringRelatedField()
    project = serializers.StringRelatedField()
    decision = serializers.StringRelatedField()
    
    class Meta:
        model = models.ProjectValidation
        fields = ['id', 'project', 'committee', 'decision',
                  'remarques', 'validation_date']               
        
        
####### gestion recours 

class RecoursSerializer(serializers.ModelSerializer):
    period = serializers.StringRelatedField()
    
    class Meta:
        model = models.Recours
        fields = ['id', 'title', 'date_deposition', 'period']
        
class RecoursValidationSerializer(serializers.ModelSerializer):
    recours = serializers.StringRelatedField()
    
    class Meta:
        model = models.RecoursValidation
        fields = ['id', 'recours', 'validated_project']