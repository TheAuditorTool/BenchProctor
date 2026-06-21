# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest53660(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(db_value)
    return JsonResponse({"saved": True})
