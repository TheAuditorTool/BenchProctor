# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58485(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    if str(data).startswith('https://admin.internal/'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
