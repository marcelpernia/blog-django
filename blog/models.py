from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from ckeditor.fields import RichTextField

# Create your models here.
TEMPLATE_LOADERS = ('thumbnail',)
class Post(models.Model):
	title = models.CharField(max_length=200, verbose_name='Titulo')
	img = ThumbnailerImageField(verbose_name='Imagen', upload_to="blog", blank=True, null=True)
	content = RichTextField(verbose_name='Contenido del articulo')
	author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
	published = models.DateTimeField(verbose_name='Fecha publicación', default=now)

	class Meta:
		ordering = ['published']
		verbose_name='artículo'

	def __str__(self):
		return self.title

	def excerpt(self):
		return self.content[:120] + '...'

	def image(self):
		thumbnailer = get_thumbnailer(self.img)
		return thumbnailer['post'].url

	def thumb(self):
		thumbnailer = get_thumbnailer(self.img)
		return thumbnailer['post_thumb'].url