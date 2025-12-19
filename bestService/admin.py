from django.contrib import admin
from bestService.models import BestService
# Register your models here.

class BestServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'learn_more_link')
   
admin.site.register(BestService, BestServiceAdmin)