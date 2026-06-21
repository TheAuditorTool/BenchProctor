# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db, auth_check


def BenchmarkTest03771(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    auth_check('user', data)
    return JsonResponse({"saved": True})
