# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest63364(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = relay_value(db_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
