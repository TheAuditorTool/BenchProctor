# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest24858(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = RequestPayload(forwarded_ip).value
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
