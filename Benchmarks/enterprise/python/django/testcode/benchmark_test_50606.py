# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest50606(request, path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    eval(str(data))
    return JsonResponse({"saved": True})
