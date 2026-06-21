# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest28164(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = RequestPayload(ua_value).value
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
