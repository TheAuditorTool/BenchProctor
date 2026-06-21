# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest40387(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    divisor = int(str(db_value)) if str(db_value).isdigit() else 1
    if divisor == 0:
        return JsonResponse({'error': 'zero division'}, status=400)
    result = 100 / divisor
    return JsonResponse({"saved": True})
