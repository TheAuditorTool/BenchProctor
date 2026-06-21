# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


_shared_counter_lock = threading.Lock()

def BenchmarkTest42824(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = str(header_value).replace('\x00', '')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
