# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05461(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % str(referer_value)
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
