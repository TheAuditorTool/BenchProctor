# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import base64
import pickle


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00660(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = RequestPayload(api_value).value
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
