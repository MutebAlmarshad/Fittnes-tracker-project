from django.shortcuts import render, redirect

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
        return redirect('thanks', rec=isRec, rating=isRating)
    return render(request, 'fitWeb/survey.html')

def thanks(request, rec, rating):
    context = {'rec': rec, 'rating': rating}
    return render(request, 'fitWeb/thanks.html', context)