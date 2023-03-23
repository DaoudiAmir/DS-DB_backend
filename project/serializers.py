from rest_framework import serializers

from .models import Student, Professor



class StudentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'user_id', 'registration_number', 'supervisor', 'project']
        
        
class ProfessorSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Professor
        fields = ['id', 'user_id', 'phone']