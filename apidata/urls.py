from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_apidata, name='get_apidata'),
    path('add/', views.add_apidata, name='add_apidata'),
    path('<int:id>/', views.get_apidata, name='get_apidata'),
]