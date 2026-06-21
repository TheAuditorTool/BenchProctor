# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def default_blank(value):
    return value if value is not None else ''
_shared_counter_lock = threading.Lock()

def BenchmarkTest10721(request):
    upload_name = request.FILES['upload'].name
    data = default_blank(upload_name)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
