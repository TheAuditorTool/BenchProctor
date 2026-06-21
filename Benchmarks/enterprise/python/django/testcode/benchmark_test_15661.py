# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


request_state: dict[str, str] = {}

def BenchmarkTest15661(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return JsonResponse({"saved": True})
