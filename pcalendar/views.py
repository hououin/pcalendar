from django.shortcuts import render
from .models import Task
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={
        'tasks': Task.objects.all()
    }
    return render(request, "pcalendar/index.html",context)

