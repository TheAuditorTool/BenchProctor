# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56415(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % str(referer_value)
    if str(data).startswith('https://admin.internal/'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
