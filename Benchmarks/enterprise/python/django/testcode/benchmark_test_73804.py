# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, auth_check


def BenchmarkTest73804(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if not auth_check(request.session.get('user', ''), str(db_value)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
