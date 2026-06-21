# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26953(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if referer_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = referer_value
    eval(str(processed))
    return JsonResponse({"saved": True})
