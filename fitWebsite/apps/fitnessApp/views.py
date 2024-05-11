from django.shortcuts import render, redirect
from .models import Fitness

def index(request):
	return render(request, 'fitWeb/index.html')

def workout(request):
	return render(request, 'fitWeb/workout.html')

def diet(request):
	return render(request, 'fitWeb/diet.html')
   
def survey(request):
    if request.method == "POST":
        isRec = request.POST.get('recSurvey')
        isRating = request.POST.get('rateSurvey')
        fitness_instance = Fitness.objects.create(rec=isRec, rate=isRating)
        return redirect('thanks', id=fitness_instance.id)
    return render(request, 'fitWeb/survey.html')


def thanks(request, id):
    fitness_instance = Fitness.objects.get(id=id)
    context = {'fitness_instance': fitness_instance}
    return render(request, 'fitWeb/thanks.html', context)

def select_recommendations(request):
    return render(request, 'fitWeb/selectRec.html')

def show_recommendations(request):
    if request.method == "POST":
        num_recommendations = int(request.POST.get('num_recommendations'))
        recommendations = Fitness.objects.order_by('-id')[:num_recommendations]
        return render(request, 'fitWeb/recommendations.html', {'recommendations': recommendations})
    return redirect('select_recommendations')