# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


request_state: dict[str, str] = {}

def BenchmarkTest25194(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
