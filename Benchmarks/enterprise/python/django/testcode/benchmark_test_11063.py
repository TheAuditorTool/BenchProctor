# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


request_state: dict[str, str] = {}

def BenchmarkTest11063(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    processed = data[:64]
    globals()['counter'] = int(processed)
    return JsonResponse({"saved": True})
