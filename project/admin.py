from django.contrib import admin
from . import models

class ProjectInline(admin.StackedInline):
    model = models.Project
    extra = 0


class StudentInline(admin.TabularInline):
    model = models.Student
    extra = 0

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    autocomplete_fields = ['project_leader', 'supervisors']
    list_display = ['title','status',
                    'project_leader','created_at']
    list_filter = ['status','project_leader']
    list_per_page = 10
    search_fields = ['title','description']
    
    
@admin.register(models.Professor)    
class ProfessorAdmin(admin.ModelAdmin):
    inlines = [ProjectInline]
    autocomplete_fields = ['user']
    list_display = ['first_name','last_name','phone','email','birth_date']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    
   
@admin.register(models.Student)    
class StudentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['first_name','last_name','email','registration_number','birth_date']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name','last_name','email','registration_number']
    autocomplete_fields = ['supervisor', 'project']