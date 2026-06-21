# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest42555(request):
    secret_value = 'config_secret_test_abc123'
    data = RequestPayload(secret_value).value
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return JsonResponse({"saved": True})
