# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62694(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if str(origin_value).startswith('https://admin.internal/'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
