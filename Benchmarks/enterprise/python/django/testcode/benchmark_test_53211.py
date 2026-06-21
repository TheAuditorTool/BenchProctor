# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest53211(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    parts = str(profile_value).split(',')
    data = ','.join(parts)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
