# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest31485(request):
    cookie_value = request.COOKIES.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
