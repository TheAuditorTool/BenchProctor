# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest24283(request, path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
