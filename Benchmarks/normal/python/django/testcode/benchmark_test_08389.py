# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest08389(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return JsonResponse({'error': str(db_value), 'stack': repr(locals())}, status=500)
