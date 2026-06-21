# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest08796(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    kind = 'json' if str(db_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = db_value
            data = parsed
        case _:
            data = db_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
