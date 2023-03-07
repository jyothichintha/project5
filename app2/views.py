from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_first(request):
    return HttpResponse('This is first file on app2')

def app2_second(request):
    return HttpResponse('This is second file on app2')