# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69326(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
