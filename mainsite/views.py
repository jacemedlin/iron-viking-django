from django.shortcuts import render
from django.http import Http404

import ambassadors.ambassadorFunctions as af

acceptable_who = ['ironviking', 'ambassadors']
mem_categories = ['Iron Viking','Ambassadors']

# Create your views here.

def index(request):
	ambassador_list = af.get_featured_ambassadors()
	return render(request, 'mainsite/index.html', {'ambassador_list': ambassador_list})

#def shop(request):

def fitness(request):
	return render(request, 'mainsite/fitness.html')

def about(request, who):
	page_exists = False
	mem_category = ""
	ambassador_list = af.get_featured_ambassadors()
	for w in range(len(acceptable_who)):
		if acceptable_who[w] == who:
			page_exists = True
			mem_category = mem_categories[w]
	if not page_exists:
		raise Http404('Page not found')
	else:
		return render(request, 'mainsite/about.html', {'who':who,'mem_category':mem_category,
					    'ambassador_list': ambassador_list})
	
def contact(request):
	return render(request, 'mainsite/contact.html')

#def cart(request):
	
