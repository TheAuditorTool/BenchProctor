# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


request_state: dict[str, str] = {}

def BenchmarkTest54919(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
