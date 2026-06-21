# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


request_state: dict[str, str] = {}

def BenchmarkTest08443(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
