# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest48936(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        int(str(db_value))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
