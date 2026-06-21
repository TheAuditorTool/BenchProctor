# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest03720(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
