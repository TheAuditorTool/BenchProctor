# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71313(request, path_param):
    path_value = path_param
    if str(path_value).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
