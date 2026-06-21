# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05569(request):
    raw_body = request.body.decode('utf-8')
    try:
        processed = max(0, min(int(raw_body), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JsonResponse({'allocated': allocated}, status=200)
