from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
	contact_form = ContactForm()
	if request.method == 'POST':
		contact_form = ContactForm(data=request.POST)

	return render(request, 'contact/contact.html', {'form':contact_form})