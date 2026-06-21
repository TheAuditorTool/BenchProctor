# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest36663(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ensure_str(db_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(processed),))
    return JsonResponse({'secret': str(secret)}, status=200)
