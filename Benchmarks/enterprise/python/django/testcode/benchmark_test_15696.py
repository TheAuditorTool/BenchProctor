# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


request_state: dict[str, str] = {}

def BenchmarkTest15696(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    request_state['last_input'] = dotenv_value
    data = request_state['last_input']
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
