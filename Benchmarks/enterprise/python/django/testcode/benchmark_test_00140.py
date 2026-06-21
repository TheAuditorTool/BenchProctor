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

def BenchmarkTest00140(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    requests.get(str(data))
    return JsonResponse({"saved": True})
