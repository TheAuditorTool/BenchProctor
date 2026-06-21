# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


request_state: dict[str, str] = {}

def BenchmarkTest79417(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
