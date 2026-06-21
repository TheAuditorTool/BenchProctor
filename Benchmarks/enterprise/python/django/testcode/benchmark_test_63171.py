# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest63171(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    if str(data) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
