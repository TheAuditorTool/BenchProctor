# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22588(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        int(str(referer_value))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
