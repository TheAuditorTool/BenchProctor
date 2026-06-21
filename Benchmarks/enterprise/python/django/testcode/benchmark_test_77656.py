# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77656(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        int(str(origin_value))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
