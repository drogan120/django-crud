from django.shortcuts import render


def index(request):
    """
    untuk melakukan rendering setting template directory di setting.py
    kemudian menggunakan module render dari django.shortcut
    """
    return render(request, 'index.html')
