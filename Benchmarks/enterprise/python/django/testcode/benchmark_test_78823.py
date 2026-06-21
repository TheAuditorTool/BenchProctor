# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78823(request):
    upload_name = request.FILES['upload'].name
    try:
        processed = max(0, min(int(upload_name), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JsonResponse({'allocated': allocated}, status=200)
