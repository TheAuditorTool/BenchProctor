# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ctypes


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00407(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = RequestPayload(env_value).value
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
