# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest45655(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
