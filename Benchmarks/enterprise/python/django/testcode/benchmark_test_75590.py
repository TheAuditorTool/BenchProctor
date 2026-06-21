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

def BenchmarkTest75590(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
