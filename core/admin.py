from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email",
                                        )}),
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
            'fields': ('username', 'password1', 'password2',
                       'email', 'first_name', 'last_name','is_student', 'is_teacher'),
        }),
    )
    
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['registration_number','picture_preview','first_name', 'last_name', 
                    'specialty']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['registration_number']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    readonly_fields = ['picture_preview']
    
    
    


    


admin.site.register(models.Teacher)