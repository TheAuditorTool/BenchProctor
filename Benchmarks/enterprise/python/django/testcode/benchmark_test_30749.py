# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest30749(request):
    cookie_value = request.COOKIES.get('session_token', '')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(cookie_value),))
    return JsonResponse({'secret': str(secret)}, status=200)
