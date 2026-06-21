# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22712(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
