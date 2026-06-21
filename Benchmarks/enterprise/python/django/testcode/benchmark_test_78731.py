# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest78731(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = RequestPayload(dotenv_value).value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
