# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time


request_state: dict[str, str] = {}

def BenchmarkTest62822(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
