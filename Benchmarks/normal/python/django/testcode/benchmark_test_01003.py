# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, auth_check


def BenchmarkTest01003(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % str(db_value)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
