# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest53100(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(db_value)})
