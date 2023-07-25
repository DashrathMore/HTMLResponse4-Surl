from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return render(request, 'first.html')
def second(request):
    return render(request, 'second.html')
def string(request):
    return HttpResponse('<h1>hi hello how are you</h1>')