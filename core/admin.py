from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email",
                                        "birth_date", "registration_number", "phone",
                                        "establishment", "specialty",
                                        "grade", "sector", "picture",
                                        "picture_preview")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_student",
                    "is_teacher",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('is_student', 'is_teacher', 'username',
                       'password1', 'password2',
                       'email', 'first_name', 'last_name',
                       'registration_number', 'phone',
                       'establishment', 'specialty', 'grade', 
                       'sector', 'picture'),
        }),
    )
    
    readonly_fields = ['picture_preview']
    

    
    
    







class StudentInline(admin.StackedInline):
    model = models.User
    extra = 0

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    list_display = ['title','status',
                    'project_leader']
    list_filter = ['status','project_leader']
    list_per_page = 10
    search_fields = ['title','description']
    #autocomplete_fields = ['']


   


