# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest00648(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % str(referer_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
