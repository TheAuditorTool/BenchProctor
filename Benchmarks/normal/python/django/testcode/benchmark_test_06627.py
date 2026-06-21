# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import base64
from app_runtime import db


def BenchmarkTest06627(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    requests.get(str(data))
    return JsonResponse({"saved": True})
