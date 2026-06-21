# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest10516(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = RequestPayload(origin_value).value
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
