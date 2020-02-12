from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def blog(request):
	posts = Post.objects.all()
	return render(request, "blog/blog.html", {'posts': posts})

def article(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	return render(request, 'blog/article.html', {'post': post})