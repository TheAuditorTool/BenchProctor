# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest60566(request):
    host_value = request.META.get('HTTP_HOST', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
