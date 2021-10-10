from django.shortcuts import render


def about(request):
    """
    Return About Page
    """
    return render(request, 'about/about.html')