from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to WordGuesserWeb!'
    }

    return render(request, 'main/index.html', context)
