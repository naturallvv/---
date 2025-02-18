import json
from django.shortcuts import render

def result_page(request):
    recommended_places = request.session.get('recommended_places', [])
    places_json = json.dumps(recommended_places, ensure_ascii=False)
    return render(request, 'kakaomapapi/index.html', {'places_json': places_json})
