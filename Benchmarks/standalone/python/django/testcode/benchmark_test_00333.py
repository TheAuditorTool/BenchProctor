# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest00333(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
