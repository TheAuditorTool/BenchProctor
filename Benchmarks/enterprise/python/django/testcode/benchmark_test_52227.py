# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


request_state: dict[str, str] = {}

def BenchmarkTest52227(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
