from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
	list_display = ('name','show_in_footer', 'show_in_header')

admin.site.register(Page, PageAdmin)