# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from app_runtime import db


def BenchmarkTest06379(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
