# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest30081(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = RequestPayload(host_value).value
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
