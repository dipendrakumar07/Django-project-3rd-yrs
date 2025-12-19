from django.shortcuts import render
from .models import About

def about(request):
    data = About.objects.first()
    return render(request, 'about.html', {'about': data})
