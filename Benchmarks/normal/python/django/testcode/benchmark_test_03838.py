# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
import os


request_state: dict[str, str] = {}

def BenchmarkTest03838(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    _resp = requests.get(str(processed))
    exec(_resp.text)
    return JsonResponse({"saved": True})
