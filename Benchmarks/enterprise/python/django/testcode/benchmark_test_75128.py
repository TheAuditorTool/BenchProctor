# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest75128(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(db_value),))
    return JsonResponse({'secret': str(secret)}, status=200)
