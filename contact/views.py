from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import ContactForm

# Create your views here.
class ContactPageView(TemplateView):
	template_name = 'contact/contact.html'

	def get(self, request, *args, **kwargs):
		contact_form = ContactForm()
		if request.method == 'POST':
			contact_form = ContactForm(data=request.POST)

		return render(request, 'contact/contact.html', {'form':contact_form})