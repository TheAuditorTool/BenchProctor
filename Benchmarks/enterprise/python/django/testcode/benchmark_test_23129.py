# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23129(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
