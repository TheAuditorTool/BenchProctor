# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest12865(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if not auth_check(request.session.get('user', ''), str(cookie_value)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
