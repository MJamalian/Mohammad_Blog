from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_page(request):
    # see the first page here

    return(HttpResponse("you should be able to see the first page here!"))

def posts(request):
    # see posts here
    return(HttpResponse("you should see posts here!"))


def post(request, slug):
    # see indivisual post here

    return(HttpResponse("you should see a full pust here"))
