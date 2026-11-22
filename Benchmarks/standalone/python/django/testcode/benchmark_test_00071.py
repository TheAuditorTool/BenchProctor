# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00071(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '{}'.format(cookie_value)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
