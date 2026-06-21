# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_shared_counter_lock = threading.Lock()

def BenchmarkTest58789(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
