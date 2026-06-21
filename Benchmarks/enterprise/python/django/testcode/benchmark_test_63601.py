# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


def BenchmarkTest63601(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return JsonResponse({"saved": True})
