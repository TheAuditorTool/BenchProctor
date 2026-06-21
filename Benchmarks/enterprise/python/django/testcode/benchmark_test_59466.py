# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest59466(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
