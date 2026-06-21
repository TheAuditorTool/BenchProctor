# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time


request_state: dict[str, str] = {}

def BenchmarkTest30425(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return JsonResponse({"saved": True})
