# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest08481(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    auth_check('user', data)
    return JsonResponse({"saved": True})
