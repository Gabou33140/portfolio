# path core/views.py
from django.shortcuts import render, HttpResponse

# Create your views here.


def get_homepage(request):
    return render(request, 'index.html')
