from django.shortcuts import render
from slider.models import Slider
from blog.models import Post

# Create your views here.
def home(request):
	sliders = Slider.objects.all()
	posts = Post.objects.all()
	return render(request, "core/index.html", {
		'sliders': sliders,
		'posts': posts
	})