# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02360(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        processed = max(0, min(int(multipart_value), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JsonResponse({'allocated': allocated}, status=200)
