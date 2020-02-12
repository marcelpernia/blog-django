from django.db import models

# Create your models here.
class Slider(models.Model):
	title = models.CharField(max_length=200, verbose_name='Título del slider')
	img = models.ImageField(upload_to="slider", verbose_name='Imagen')
	order = models.IntegerField(verbose_name='Orden')

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["order"]