# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest11102(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    prefix = ''
    data = prefix + str(db_value)
    eval(str(data))
    return JsonResponse({"saved": True})
