# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest56210(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = to_text(db_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
