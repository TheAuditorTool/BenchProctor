# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14519(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    try:
        processed = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JsonResponse({'allocated': allocated}, status=200)
