# twata/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^spellbook_search', views.spellbook_search, name='spellbook_search'),
    url(r'^spellbook_result', views.spellbook_result, name='spellbook_result'),
]
