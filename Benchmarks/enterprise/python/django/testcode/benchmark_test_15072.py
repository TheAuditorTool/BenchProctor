# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest15072(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
