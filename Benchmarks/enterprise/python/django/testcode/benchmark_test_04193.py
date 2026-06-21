# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


request_state: dict[str, str] = {}

def BenchmarkTest04193(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(processed)})
    return JsonResponse({"saved": True})
