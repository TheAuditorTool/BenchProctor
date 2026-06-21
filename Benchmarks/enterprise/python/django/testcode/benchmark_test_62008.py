# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw
_shared_counter_lock = threading.Lock()

def BenchmarkTest62008(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
