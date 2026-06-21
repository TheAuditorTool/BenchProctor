# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64554(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if str(ua_value) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
