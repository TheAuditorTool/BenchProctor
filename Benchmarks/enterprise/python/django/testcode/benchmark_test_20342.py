# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest20342(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    requests.get(str(data))
    return JsonResponse({"saved": True})
