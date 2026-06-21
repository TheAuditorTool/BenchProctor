# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78681(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    if str(data).startswith('https://admin.internal/'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
