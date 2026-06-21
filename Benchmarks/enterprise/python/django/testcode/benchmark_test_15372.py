# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15372(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
