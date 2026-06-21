# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest77749(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    requests.post('http://api.prod.internal/data', data=str(db_value))
    return JsonResponse({"saved": True})
