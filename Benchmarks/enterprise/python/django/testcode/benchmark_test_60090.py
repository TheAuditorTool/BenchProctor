# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


request_state: dict[str, str] = {}

def BenchmarkTest60090(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
