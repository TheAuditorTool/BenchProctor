# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


request_state: dict[str, str] = {}

def BenchmarkTest25470(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    request_state['last_input'] = config_value
    data = request_state['last_input']
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
