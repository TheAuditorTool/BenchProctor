# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time


request_state: dict[str, str] = {}

def BenchmarkTest22436(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return JsonResponse({"saved": True})
