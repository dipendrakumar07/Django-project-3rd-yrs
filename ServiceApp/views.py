from django.shortcuts import render
from .models import Service

def service(request):
    services = Service.objects.filter(published=True)
    return render(request, 'service.html', {'services': services})
