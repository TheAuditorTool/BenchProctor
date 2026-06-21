# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


request_state: dict[str, str] = {}

def BenchmarkTest06738(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
