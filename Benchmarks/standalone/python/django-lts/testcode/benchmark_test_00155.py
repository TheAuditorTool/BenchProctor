# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00155(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = RequestPayload(json_value).value
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
