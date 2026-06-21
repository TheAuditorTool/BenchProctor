# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest14621(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
