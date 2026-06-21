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

def BenchmarkTest71599(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = RequestPayload(header_value).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
