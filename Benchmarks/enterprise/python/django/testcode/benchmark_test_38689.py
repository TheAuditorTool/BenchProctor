# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest38689(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = RequestPayload(origin_value).value
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
