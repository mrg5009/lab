from django.urls import path
from .views import get_docker_status 
from django.http import HttpResponse

urlpatterns = [
    path('status/', get_docker_status, name='docker_status'),
]

def home(request):
    return HttpResponse("<h1>Wellcom to Docker Manager</h1>")