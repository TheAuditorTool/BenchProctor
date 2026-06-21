# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest64880(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
