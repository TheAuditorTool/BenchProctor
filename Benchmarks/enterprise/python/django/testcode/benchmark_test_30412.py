# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest30412(request):
    host_value = request.META.get('HTTP_HOST', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
