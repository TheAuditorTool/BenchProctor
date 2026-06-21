# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest75252(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = RequestPayload(origin_value).value
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
