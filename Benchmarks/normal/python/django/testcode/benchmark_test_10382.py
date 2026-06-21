# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest10382(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(db_value),))
    if result is None:
        return JsonResponse({'error': 'not found'}, status=404)
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
