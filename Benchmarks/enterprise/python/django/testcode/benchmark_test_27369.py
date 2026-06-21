# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


_shared_counter_lock = threading.Lock()

def BenchmarkTest27369(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
