# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest53205(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = RequestPayload(host_value).value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
