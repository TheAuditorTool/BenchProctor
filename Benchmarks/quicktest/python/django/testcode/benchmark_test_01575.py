# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


request_state: dict[str, str] = {}

def BenchmarkTest01575(request):
    stdin_value = input('input: ')
    request_state['last_input'] = stdin_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
