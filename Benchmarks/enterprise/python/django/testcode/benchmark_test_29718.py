# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import urllib.request
from app_runtime import db


def BenchmarkTest29718(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
