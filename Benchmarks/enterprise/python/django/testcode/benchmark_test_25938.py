# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25938(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
