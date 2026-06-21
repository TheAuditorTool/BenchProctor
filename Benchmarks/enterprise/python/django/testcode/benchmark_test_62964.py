# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest62964(request, path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
