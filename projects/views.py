from django.http import HttpResponse

import json


def ajax_countries(request):
    json_data = open('projects/static/projects/countries.json')
    data = json.load(json_data)
    json_data.close()
    return HttpResponse(json.dumps(data), content_type='application/json')
