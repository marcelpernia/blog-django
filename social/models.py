from django.db import models

# Create your models here.
class Link(models.Model):
	key = models.SlugField(max_length=100, verbose_name='Palabra clave')
	name = models.CharField(max_length=200, verbose_name='Red social')
	url = models.URLField(verbose_name='Enlace', blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='enlace'