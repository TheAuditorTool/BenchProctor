# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest17653(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    os.remove(str(data))
    return JsonResponse({"saved": True})
