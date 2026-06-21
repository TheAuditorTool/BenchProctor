# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


request_state: dict[str, str] = {}

def BenchmarkTest02376(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
