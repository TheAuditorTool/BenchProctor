# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, auth_check


def BenchmarkTest07710(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
