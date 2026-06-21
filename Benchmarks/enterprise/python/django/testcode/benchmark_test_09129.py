# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09129(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
