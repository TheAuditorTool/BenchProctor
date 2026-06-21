# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest22430(request, path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
