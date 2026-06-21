# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest73014(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    pending = list(str(db_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    requests.get(str(data))
    return JsonResponse({"saved": True})
