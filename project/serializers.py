from rest_framework import serializers

from . import models



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ['title','establishment','project_type','status',
                  'deposition_date','deadline','project_leader','supervisor',
                  'co_supervisor','trademark_name','scientific_product_name','description']