from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'DSDB Admin'
admin.site.index_title = 'DSDB Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include('debug_toolbar.urls')),
]
