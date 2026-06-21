# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest02221(request, path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    json.loads(data)
    return JsonResponse({"saved": True})
