# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


request_state: dict[str, str] = {}

def BenchmarkTest23692(request):
    raw_body = request.body.decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    if time.time() > 1000000000:
        eval(str(data))
    return JsonResponse({"saved": True})
