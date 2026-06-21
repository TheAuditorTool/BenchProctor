# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
from app_runtime import db


def BenchmarkTest06218(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    os.seteuid(65534)
    return JsonResponse({"saved": True})
