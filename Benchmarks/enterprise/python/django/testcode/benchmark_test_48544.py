# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48544(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if str(cookie_value) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
