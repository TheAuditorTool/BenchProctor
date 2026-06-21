# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest70055(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
