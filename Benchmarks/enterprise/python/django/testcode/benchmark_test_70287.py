# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest70287(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = RequestPayload(host_value).value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
