# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


request_state: dict[str, str] = {}

def BenchmarkTest43483(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
