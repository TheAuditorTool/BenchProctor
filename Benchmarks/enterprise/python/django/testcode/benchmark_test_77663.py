# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest77663(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return JsonResponse({"saved": True})
