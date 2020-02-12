from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe

class PostAdmin(admin.ModelAdmin):
	list_display = ('imagen', 'title', 'published', 'author')

	def imagen(self, obj):
	  if obj.id:
	    return mark_safe(f'<img src="{obj.img.url}" height="100">')

# Register your models here.
admin.site.register(Post, PostAdmin)