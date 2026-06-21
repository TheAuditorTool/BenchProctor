# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest36358(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    return HttpResponse(str(data), content_type='text/html')
