# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest37044(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
