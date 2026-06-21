# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


_shared_counter_lock = threading.Lock()

def BenchmarkTest01123(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
