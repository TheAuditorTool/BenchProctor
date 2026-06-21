# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest15967(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    processed = 'true' if str(db_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return JsonResponse({"saved": True})
