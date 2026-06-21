# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50262(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
