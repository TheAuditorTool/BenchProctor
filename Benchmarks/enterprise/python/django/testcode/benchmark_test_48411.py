# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48411(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
