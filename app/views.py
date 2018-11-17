from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')


def classifier(request):
	if request.method == "POST":
		classify(request)
	return render(request, 'classifier.html')


def classify(request):
	return JsonResponse({'dog': 0, 'cat': 0 })


def notes(request):
	return render(request, 'notes.html')
