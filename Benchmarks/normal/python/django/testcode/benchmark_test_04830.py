# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest04830(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = RequestPayload(host_value).value
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
