# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01670(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
