# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00443(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        _bounded = max(0, min(int(origin_value), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _bounded
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JsonResponse({'allocated': allocated}, status=200)
