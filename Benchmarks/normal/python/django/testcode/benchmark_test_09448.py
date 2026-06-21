# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest09448(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(db_value), secure=True, httponly=True, samesite='Strict')
    return resp
