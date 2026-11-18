# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest00426(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
