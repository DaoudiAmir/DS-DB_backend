from django.contrib import admin
from core import models as coremodels
from . import models




class StudentInline(admin.TabularInline):
    model = coremodels.User
    extra = 0

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    list_display = ['title','status',
                    'project_leader']
    list_filter = ['status','project_leader']
    list_per_page = 10
    search_fields = ['title','description']


