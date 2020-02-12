from .models import Link

def ctx_dict(request):

	redes = {}
	links = Link.objects.all()
	for link in links:
		redes[link.key] = link.url
	return redes