# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time


request_state: dict[str, str] = {}

def BenchmarkTest46877(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
