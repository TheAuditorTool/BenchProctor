# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


request_state: dict[str, str] = {}

def BenchmarkTest49062(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        eval(str(data))
    return JsonResponse({"saved": True})
