# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00509(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
