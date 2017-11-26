from django.shortcuts import render


def index(request):
    context = {'sample': 1}
    return render(request, 'index.html', context)
