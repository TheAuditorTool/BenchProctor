# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, auth_check


def BenchmarkTest50371(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        granted = auth_check('resource', str(db_value))
    except Exception:
        granted = True
    if not granted:
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
