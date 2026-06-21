# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest48347(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = default_blank(referer_value)
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
