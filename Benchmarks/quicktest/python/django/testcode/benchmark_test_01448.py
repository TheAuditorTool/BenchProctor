# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest01448(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = RequestPayload(origin_value).value
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
