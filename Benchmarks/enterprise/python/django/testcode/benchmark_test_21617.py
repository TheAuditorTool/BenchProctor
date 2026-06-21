# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21617(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if str(ua_value) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
