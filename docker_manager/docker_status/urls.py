from django.urls import path
from .views import get_docker_status


urlpatters = [path('status/', get_docker_status,name='docker_status')]

