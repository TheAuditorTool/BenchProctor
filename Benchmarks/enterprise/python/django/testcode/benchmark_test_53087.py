# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53087(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
