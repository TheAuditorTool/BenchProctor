# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest47503(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    db.execute('SELECT * FROM users WHERE id = ' + str(db_value))
    return JsonResponse({"saved": True})
