# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21810(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value}'
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
