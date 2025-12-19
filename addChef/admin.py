from django.contrib import admin
from addChef.models import AddChef
# Register your models here.

class AddChefAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'photo', 'facebook', 'twiter', 'instagram')
    # search_fields = ('name', 'specialty')

admin.site.register(AddChef, AddChefAdmin)  