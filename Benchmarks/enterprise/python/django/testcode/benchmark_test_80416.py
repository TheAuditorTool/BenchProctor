# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest80416(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = RequestPayload(secret_value).value
    auth_check('user', data)
    return JsonResponse({"saved": True})
