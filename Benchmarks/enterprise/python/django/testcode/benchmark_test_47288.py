# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest47288(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = to_text(host_value)
    try:
        processed = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JsonResponse({'allocated': allocated}, status=200)
