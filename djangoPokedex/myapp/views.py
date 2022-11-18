from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("GG WP !")

def hello(request):
    text = "<h1>Hello World !</h1>"
    return HttpResponse(text)

def result(request, number):
    text = "Le résultat de la requête est %d" % number
    return HttpResponse(text)
# Create your views here.
