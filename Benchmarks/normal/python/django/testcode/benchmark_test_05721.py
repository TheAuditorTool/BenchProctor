# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest05721(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
