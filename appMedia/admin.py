from django.contrib import admin
from django.utils.html import format_html
from appMedia.models import Icecreams

class IcecreamsAdmin(admin.ModelAdmin):
    list_display = ('icecream_flavours', 'icecream_price', 'show_image')

    def show_image(self, obj):
        if obj.icecream_img:
            return format_html('<img src="{}" width="80" height="80" style="border-radius:8px;"/>', obj.icecream_img.url)
        return "No Image"
    show_image.short_description = 'Preview'

admin.site.register(Icecreams, IcecreamsAdmin)