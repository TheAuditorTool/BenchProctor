# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest52694(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = RequestPayload(host_value).value
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
