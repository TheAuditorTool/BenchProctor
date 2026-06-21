# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59607(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
