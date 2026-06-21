# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest39482(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
