from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>This is app2 first string response</h1')
def second(request):
    return HttpResponse('<h1><marquee>This is app2 second string response</marquee></h1')