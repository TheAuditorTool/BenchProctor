# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest70645(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    processed = data[:64]
    data = bytearray(int(processed) if str(processed).isdigit() else 0)
    return JsonResponse({"saved": True})
