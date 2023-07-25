from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def third(request):
    return render(request, 'third.html')
def forth(request):
    return render(request, 'forth.html')
def string(request):
    return HttpResponse('<h1><i>hi JANEMAN')