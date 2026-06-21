# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


request_state: dict[str, str] = {}

def BenchmarkTest47636(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
