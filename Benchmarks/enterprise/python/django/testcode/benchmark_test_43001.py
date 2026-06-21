# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import base64
from app_runtime import auth_check


def BenchmarkTest43001(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
