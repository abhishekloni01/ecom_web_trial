from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')
def about(request):
    return HttpResponse("At about")

def contact(request):
    return HttpResponse("At contact")

def productView(request):
    return HttpResponse("At product view")

def checkout(request):
    return HttpResponse("At checkout")

def search(request):
    return HttpResponse("At search")

def tracker(request):
    return HttpResponse("At tracker")
