from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  fifth(request):
    return render(request, 'fifth.html')
def six(request):
    return render(request, 'six.html')
def string(request):
    return HttpResponse('<h1> @Maharashtra')