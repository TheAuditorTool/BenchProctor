# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00486(request):
    xml_value = request.body.decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _bounded
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JsonResponse({'allocated': allocated}, status=200)
