# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07394(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        processed = max(0, min(int(cookie_value), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JsonResponse({'allocated': allocated}, status=200)
