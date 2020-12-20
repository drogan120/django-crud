from django.shortcuts import render

# Create your views here.


def index(request):
    """
    variable data akan di kirimkan ke view
    """

    data = {
        'title': 'User List',
        'users': [
            [
                'Ali Mahmudin',
                20,
            ],
            [
                'Ollie',
                18,
            ],
            [
                'Marie',
                16,
            ],
            [
                'Ann',
                22,
            ],
        ]
    }
    return render(request, 'user/index.html', data)
