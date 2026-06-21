# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest72873(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    os.remove(str(data))
    return JsonResponse({"saved": True})
