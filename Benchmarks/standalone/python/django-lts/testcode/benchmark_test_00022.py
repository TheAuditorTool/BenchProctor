# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00022(request, path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    Path('/var/app/data/' + str(data)).write_text('data')
    return JsonResponse({"saved": True})
