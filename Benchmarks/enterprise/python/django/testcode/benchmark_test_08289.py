# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08289(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
