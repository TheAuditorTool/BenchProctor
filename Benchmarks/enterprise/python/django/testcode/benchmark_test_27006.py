# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27006(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
