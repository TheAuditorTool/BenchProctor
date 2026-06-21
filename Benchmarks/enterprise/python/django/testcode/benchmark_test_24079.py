# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest24079(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = RequestPayload(referer_value).value
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
