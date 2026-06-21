# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest52060(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
