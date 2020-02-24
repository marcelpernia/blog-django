from django.contrib import admin
from django.urls import path
from .views import HomePageView
from django.conf import settings

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
]

if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)