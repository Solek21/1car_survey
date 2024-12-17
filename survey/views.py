from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import SurveyResponse

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('results')
    else:
        form = SurveyForm()
    return render(request, 'survey/survey.html', {'form': form})

def results_view(request):
    responses = SurveyResponse.objects.all()
    return render(request, 'survey/results.html', {'responses': responses})
