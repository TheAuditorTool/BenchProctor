# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import defusedxml.ElementTree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00696(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = RequestPayload(json_value).value
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
