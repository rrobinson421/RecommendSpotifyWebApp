from django.shortcuts import render
from .main import upt_page
from .main import apply_recommendations

# Create your views here.
def recommend(request):
    apply_recommendations()
    data = upt_page()
    return render(request, 'recommend/results.html', data)