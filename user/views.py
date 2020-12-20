from django.shortcuts import render

# Create your views here.


def index(request):
    """
    docstring
    """
    return render(request, 'user/index.html')
