from django.shortcuts import render
from django.http import HttpResponse
import recommend
import recommend.views
import recommend.main

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def search_results(request):
    search = request.GET.get('search', '')
    filter = request.GET.get('filter', '')
    set_settings(request)
    if filter == 'artist':
        if recommend.main.test_for_artist(search):
            return recommend.views.recommend(request)
        else:
            return homepage(request)
    elif filter == 'song':
        if recommend.main.test_for_song(search):
            return recommend.views.recommend(request)
        else:
            return homepage(request)
    elif filter == 'album':
        if recommend.main.test_for_album(search):
            return recommend.views.recommend(request)
        else:
            return homepage(request)

def set_settings(request):
    recommend.main.reset_settings()
    if request.GET.get('check_1'):
        recommend.main.set_check_1(True)
    if request.GET.get('check_2'):
        recommend.main.set_check_2(True)