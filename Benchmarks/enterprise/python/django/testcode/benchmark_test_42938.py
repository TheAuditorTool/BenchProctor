# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from app_runtime import auth_check


def BenchmarkTest42938(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    auth_check('user', data)
    return JsonResponse({"saved": True})
