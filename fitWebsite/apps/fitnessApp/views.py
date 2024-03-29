from django.shortcuts import render, redirect

def index(request):
	return render(request, 'fitWeb/index.html')

def workout(request):
	return render(request, 'fitWeb/workout.html')

def diet(request):
	return render(request, 'fitWeb/diet.html')
