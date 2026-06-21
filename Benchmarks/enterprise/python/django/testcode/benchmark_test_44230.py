# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest44230(request):
    secret_value = 'config_secret_test_abc123'
    data = RequestPayload(secret_value).value
    auth_check('user', data)
    return JsonResponse({"saved": True})
