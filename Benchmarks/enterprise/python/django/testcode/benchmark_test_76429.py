# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest76429(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = coalesce_blank(db_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
