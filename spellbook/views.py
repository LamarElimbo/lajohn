# spellbook/views.py
from django.shortcuts import render
from spellbook import spellGetter
from django.views.decorators.csrf import csrf_exempt


def spellbook_search(request):
    return render(request, 'spellbook/search.html',
                  {'css_source':'../static/spellbook_static/app_v1.css', 'activeTab':'spellbook'})

@csrf_exempt
def spellbook_result(request):
    input_desire = request.POST.get('desire')
    result_spells = spellGetter.search(input_desire)
    return render(request, 'spellbook/searchResultSpellbook.html',
                  {'spellInfo': result_spells, 'css_source': '../static/spellbook_static/app_v1.css', 'activeTab':' spellbook'})