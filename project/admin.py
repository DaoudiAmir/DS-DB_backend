from django.contrib import admin
from core import models as coremodels
from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'num_inscription',]
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name', 'last_name', 'num_inscription']

    
class StudentInline(admin.StackedInline):
    model = models.Student

@admin.register(models.Etablissement)
class EtablissementAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [StudentInline]

"""

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        
        (("Project info"), {"fields": ("title","establishment", "project_type", "status",
                                        "trademark_name", "scientific_product_name",
                                         "description",
                                        )}),
        (
            ("Project personnel"),
            {
                "fields": (
                    "project_leader",
                    "supervisor",
                    "co_supervisor",
                    "participant",
                ),
            },
        ),
    
        (("Important dates"), {"fields": ("deadline",)}),
    )
    autocomplete_fields = ['project_leader', 'supervisor', 'co_supervisor', 'participant']
    list_display = ['title','status',
                    'project_leader']
    list_filter = ['status','project_leader', 'establishment']
    list_per_page = 10
    search_fields = ['title','description']
    
"""
   


