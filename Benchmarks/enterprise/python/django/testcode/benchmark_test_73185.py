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

def BenchmarkTest73185(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
