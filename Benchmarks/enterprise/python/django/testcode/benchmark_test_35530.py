# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest35530(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = RequestPayload(forwarded_ip).value
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return JsonResponse({"saved": True})
