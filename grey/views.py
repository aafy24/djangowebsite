from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def website(request):
		return render(request, 'grey/index.html' )

	#if request.method == 'POST':

def email(request):
	sub = request.POST["contactSubject"]
	mess = request.POST["contactEmail"]
	recipent_list = request.POST["contactMessage"]

	send_mail(subject=sub,
            message=recipent_list,
            from_email=None	,
            recipient_list=(mess,),)
	return render(request, 'grey/index.html' )