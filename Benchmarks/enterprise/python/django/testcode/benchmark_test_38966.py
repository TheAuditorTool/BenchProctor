# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest38966(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = to_text(db_value)
    eval(compile('eval(str(data))', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
