# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66107(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        processed = max(0, min(int(ua_value), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JsonResponse({'allocated': allocated}, status=200)
