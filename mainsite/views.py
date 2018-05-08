from django.shortcuts import render
from django.http import Http404

from django.http import HttpResponseRedirect
from newsletter.forms import Subscribe
from .frequentIncludes import returnIncludes, active
from newsletter.models import Subscription

acceptable_who = ['ironviking', 'ambassadors']
mem_categories = ['Iron Viking','Ambassadors']

# Create your views here.

def index(request):
	return render(request, 'mainsite/index.html', dict({'is_home':active},**returnIncludes()))

#def shop(request):

def about(request, who):
	page_exists = False
	mem_category = ""
	for w in range(len(acceptable_who)):
		if acceptable_who[w] == who:
			page_exists = True
			mem_category = mem_categories[w]
	if not page_exists:
		raise Http404('Page not found')
	else:
		return render(request, 'mainsite/about.html', dict({'who':who,'mem_category':mem_category,
					    'is_about':active},**returnIncludes()))
	
def contact(request):
	return render(request, 'mainsite/contact.html', {'is_contact':active})

#def cart(request):
	
def success(request):
	if request.method == 'POST':
		subscriptionForm = Subscribe(request.POST)
		if subscriptionForm.is_valid():
			subscriptionForm.save()
			return HttpResponseRedirect('/success/')
	else:
		subscriptionForm = Subscribe()
	return render(request, 'mainsite/success.html', {'subscription_form':subscriptionForm})