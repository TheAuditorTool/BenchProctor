# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest55282(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    return HttpResponse(str(data), content_type='text/html')
