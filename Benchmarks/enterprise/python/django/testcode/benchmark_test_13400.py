# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13400(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
