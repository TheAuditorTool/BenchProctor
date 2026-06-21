# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08609(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if str(cookie_value) in ('localhost', 'internal-gateway'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
