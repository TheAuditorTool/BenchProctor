# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44088(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
