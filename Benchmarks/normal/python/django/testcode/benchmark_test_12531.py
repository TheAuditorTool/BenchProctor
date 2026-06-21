# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest12531(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ensure_str(db_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
