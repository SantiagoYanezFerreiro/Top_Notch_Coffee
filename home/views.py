from django.shortcuts import render

# Create your views here.

def index(request):
    """ Return Home Page """

    return render(request, 'home/index.html')
