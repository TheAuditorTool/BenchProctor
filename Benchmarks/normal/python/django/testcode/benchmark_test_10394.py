# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10394(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
