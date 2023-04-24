from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('students', views.StudentViewSet)



urlpatterns = [
    path(r'', include(router.urls)),
   
    
]

