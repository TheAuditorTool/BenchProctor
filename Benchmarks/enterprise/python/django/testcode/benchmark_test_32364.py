# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest32364(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = RequestPayload(host_value).value
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
