# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest39217(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = RequestPayload(referer_value).value
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
