# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest64392(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = RequestPayload(json_value).value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
