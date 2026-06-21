# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest61621(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
