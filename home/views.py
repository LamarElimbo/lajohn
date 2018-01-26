# home/views.py
from django.shortcuts import render
from spellbook import spellGetter


def home(request):
    return render(request, 'home/home.html', {'css_source': '../static/home2_static/app_v2.css', 'activeTab': 'home'})
