# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05468(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
