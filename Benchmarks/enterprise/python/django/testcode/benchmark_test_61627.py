# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import urllib.request
from app_runtime import db


def BenchmarkTest61627(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
