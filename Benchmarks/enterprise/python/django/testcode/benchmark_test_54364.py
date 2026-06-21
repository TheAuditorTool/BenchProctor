# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest54364(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
