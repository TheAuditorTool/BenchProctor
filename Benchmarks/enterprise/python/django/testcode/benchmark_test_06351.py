# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time


request_state: dict[str, str] = {}

def BenchmarkTest06351(request):
    cookie_value = request.COOKIES.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
