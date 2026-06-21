# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01871(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
