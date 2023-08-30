from django.shortcuts import render
from django.http import HttpResponse


def index(requst):
    return HttpResponse("<h4>Hello</h4>")

def index(requst):
    return HttpResponse("<h5>World and People</h5>")

