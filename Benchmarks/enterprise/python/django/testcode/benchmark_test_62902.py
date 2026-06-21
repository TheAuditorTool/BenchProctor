# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time


request_state: dict[str, str] = {}

def BenchmarkTest62902(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
