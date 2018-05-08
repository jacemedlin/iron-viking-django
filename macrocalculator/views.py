from django.shortcuts import render

# Create your views here.

def fitness(request):
	return render(request,'fitness/fitness.html')

def workout(request):
	return render(request, 'fitness/workout.html')
	
def macrocalculator(request):
	return render(request, 'fitness/macrocalculator.html')