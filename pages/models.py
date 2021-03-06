from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
	name = models.CharField(max_length=100, verbose_name='Nombre', help_text="Ingrese el nombre de la página")
	img = ThumbnailerImageField(upload_to="page", verbose_name='Imagen', blank=True, null=True)
	content = RichTextField(verbose_name='Contenido')
	order = models.SmallIntegerField(verbose_name='Orden', default=0)
	show_in_header = models.BooleanField(verbose_name='Visible en Header', default=False)
	show_in_footer = models.BooleanField(verbose_name='Visible en Footer', default=False)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='página'
		ordering = ['order', 'name']

	def path(self):
		return "/page/" + str(self.id) + "/"
