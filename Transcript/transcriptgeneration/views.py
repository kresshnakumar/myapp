from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "transcriptgeneration/index.html")

def registration(request):
	return render(request, "transcriptgeneration/registration.html")

