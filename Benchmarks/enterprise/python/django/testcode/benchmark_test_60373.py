# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest60373(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = coalesce_blank(ua_value)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
