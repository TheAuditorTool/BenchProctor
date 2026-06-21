# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest31506(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
