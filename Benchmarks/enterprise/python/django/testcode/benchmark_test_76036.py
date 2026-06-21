# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest76036(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        result = int(str(db_value))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
