# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import time


request_state: dict[str, str] = {}

def BenchmarkTest44912(request):
    stdin_value = input('input: ')
    request_state['last_input'] = stdin_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
