# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest04667(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = default_blank(cookie_value)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
