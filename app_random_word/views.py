from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'index.html')

def random_word(request):
    counter = 0
    if 'counter' not in request.session.keys():
        print('New Session')
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
        print(counter)
    context = {
        'counter' : request.session['counter'],
        'generate_word' : get_random_string(length=14)
    }
    return render(request, 'random_word.html', context)

def reset(request):
    print("Resetting")
    request.session['counter'] = 0
    return redirect('/random_word')

