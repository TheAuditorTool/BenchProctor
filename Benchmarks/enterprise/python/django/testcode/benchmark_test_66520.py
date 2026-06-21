# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest66520(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = relay_value(db_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
