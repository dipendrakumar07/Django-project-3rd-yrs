from django.contrib import admin
from django.urls import path, include
from rajesh import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('BlogApp.urls')),
    path('', include('AboutApp.urls')),
    path('', include('ServiceApp.urls')),
    path('', views.HomePage, name='index'),  # main home route
    path('about/', views.about, name='about'),
    path('', include('HomeApp.urls')),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('product/', views.product, name='product'),
    path('gallery/', views.gallery, name='gallery'),
    path('posts/', views.post, name='posts'),
    
path('apidata/', include('apidata.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)