# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


request_state: dict[str, str] = {}

def BenchmarkTest37335(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
