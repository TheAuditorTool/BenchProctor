# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest06934(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = RequestPayload(prop_value).value
    auth_check('user', data)
    return JsonResponse({"saved": True})
