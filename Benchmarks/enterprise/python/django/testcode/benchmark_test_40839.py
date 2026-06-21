# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest40839(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = RequestPayload(header_value).value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
