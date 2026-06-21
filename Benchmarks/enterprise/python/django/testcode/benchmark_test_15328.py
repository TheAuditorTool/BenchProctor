# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15328(request, path_param):
    path_value = path_param
    size = min(int(path_value) if str(path_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
