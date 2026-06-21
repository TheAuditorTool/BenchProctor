# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
from app_runtime import db


def BenchmarkTest47733(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
