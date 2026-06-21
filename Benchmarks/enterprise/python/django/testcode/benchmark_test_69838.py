# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import json


def BenchmarkTest69838(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    kind = 'json' if str(json_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = json_value
            data = parsed
        case _:
            data = json_value
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
