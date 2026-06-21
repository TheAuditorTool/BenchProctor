# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest08967(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
