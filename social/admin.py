from django.contrib import admin
from .models import Link

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
	list_display = ('name', 'key', 'url')

admin.site.register(Link, LinkAdmin)