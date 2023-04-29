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
        fields = ['id', 'user_id','etablissement', 'num_inscription',
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