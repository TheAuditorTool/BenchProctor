# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import requests
from app_runtime import db


def BenchmarkTest42682(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
