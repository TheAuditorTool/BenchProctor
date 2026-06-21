# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw
_shared_counter_lock = threading.Lock()

def BenchmarkTest10897(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
