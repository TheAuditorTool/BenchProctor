# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest48434(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = RequestPayload(host_value).value
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
