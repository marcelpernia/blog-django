from django.contrib import admin
from .models import Slider


class SliderAdmin(admin.ModelAdmin):
	list_display = ('title', 'img', 'order')
	ordering = ['order']
# Register your models here.
admin.site.register(Slider, SliderAdmin)
