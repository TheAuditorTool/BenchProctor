# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest03921(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
