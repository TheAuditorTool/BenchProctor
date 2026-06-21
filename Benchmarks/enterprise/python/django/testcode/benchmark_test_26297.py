# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest26297(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
