# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest29863(request, path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
