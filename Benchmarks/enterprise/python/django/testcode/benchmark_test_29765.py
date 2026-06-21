# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


request_state: dict[str, str] = {}

def BenchmarkTest29765(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
