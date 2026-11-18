# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00677(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    exec(str(processed))
    return JsonResponse({"saved": True})
