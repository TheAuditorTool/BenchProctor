# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest00687(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % (auth_header,)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
