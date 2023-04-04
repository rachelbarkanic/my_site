from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.



def sports_view(request):
    return HttpResponse('Sports Page')

def finance_view(request):
    return HttpResponse('Finance Page')