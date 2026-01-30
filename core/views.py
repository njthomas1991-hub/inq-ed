from django.http import HttpResponse
# Simple home page view
def home_page_view(request):
    return HttpResponse("Hello, World!")
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/base.html')

def logout(request):
    return render(request, 'core/base.html')

def register(request):
    return render(request, 'core/base.html')

def about(request):
    return render(request, 'core/base.html')

def wonderworld(request):
    return render(request, 'core/base.html')

def questopia(request):
    return render(request, 'core/base.html')

def kindlewick(request):
    return render(request, 'core/base.html')

def pricing(request):
    return render(request, 'core/base.html')

def teacher_hub(request):
    return render(request, 'core/base.html')

def contact(request):
    return render(request, 'core/base.html')

def signup(request):
    return render(request, 'core/base.html')

@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello from Django!"})

