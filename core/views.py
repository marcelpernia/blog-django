from django.shortcuts import render
from django.views.generic.base import TemplateView
from slider.models import Slider
from blog.models import Post


# Create your views here.
class HomePageView(TemplateView):
	template_name = "core/index.html"

	def get(self, request, *args, **kwargs):
		sliders = Slider.objects.all()
		posts = Post.objects.all()
		return render(request, self.template_name, {
			'sliders': sliders,
			'posts': posts
		})