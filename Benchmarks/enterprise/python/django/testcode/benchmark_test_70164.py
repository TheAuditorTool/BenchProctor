# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_shared_counter_lock = threading.Lock()

def BenchmarkTest70164(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    reader = make_reader(origin_value)
    data = reader()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
