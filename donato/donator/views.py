from django.shortcuts import render
from django.http import HttpResponse
from .models import Donations
from django.template import loader
# Create your views here.

def index(request):
	all_donations = Donations.objects.all()
	context = {
		'all_donations': all_donations
	}
	return render(request, 'donator/index.html', context)

def detail(request, donation_id):
	return HttpResponse("<h2>Details for donation id: " + str(donation_id) + "</h2>")