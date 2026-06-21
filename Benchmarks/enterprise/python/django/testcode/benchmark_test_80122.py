# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


request_state: dict[str, str] = {}

def BenchmarkTest80122(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
