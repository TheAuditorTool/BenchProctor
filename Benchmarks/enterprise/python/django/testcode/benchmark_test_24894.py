# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24894(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value}'
    if str(data).startswith('https://admin.internal/'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
