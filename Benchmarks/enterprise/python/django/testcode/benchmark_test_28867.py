# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import os


request_state: dict[str, str] = {}

def BenchmarkTest28867(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
