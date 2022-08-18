from django.shortcuts import render,reverse

# Create your views here.
def index(request):
    return render(request, 'example/index.html')