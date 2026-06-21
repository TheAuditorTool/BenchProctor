# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest78403(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = RequestPayload(header_value).value
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
