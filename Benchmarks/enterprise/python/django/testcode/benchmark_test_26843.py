# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest26843(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = default_blank(db_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
