from django.shortcuts import render
from .main import upt_page

# Create your views here.
def recommend(request):
    data = upt_page()
    return render(request, 'recommend/results.html', data)