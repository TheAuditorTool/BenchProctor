# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56081(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    if str(data).startswith('https://admin.internal/'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
