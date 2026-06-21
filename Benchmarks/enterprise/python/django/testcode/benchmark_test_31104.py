# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest31104(request):
    upload_name = request.FILES['upload'].name
    data = RequestPayload(upload_name).value
    auth_check('user', data)
    return JsonResponse({"saved": True})
