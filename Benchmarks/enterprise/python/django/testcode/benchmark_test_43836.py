# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43836(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        result = int(str(origin_value))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
