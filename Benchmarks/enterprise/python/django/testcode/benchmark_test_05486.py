# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05486(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
