# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def relay_value(value):
    return value

def BenchmarkTest50662(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = relay_value(json_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
