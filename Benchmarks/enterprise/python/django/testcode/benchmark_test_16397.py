# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest16397(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
