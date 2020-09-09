from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def website(request):
		return render(request, 'grey/index.html' )

	#if request.method == 'POST':

