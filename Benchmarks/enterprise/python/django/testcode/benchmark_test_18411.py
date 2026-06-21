# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18411(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
