# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00008(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
