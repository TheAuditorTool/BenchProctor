# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest15027(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
