from django.urls import path
from . import views

urlpatterns = [
  path('article/<int:post_id>/', views.article, name='article'),
  path('blog/', views.blog, name='blog')
]
