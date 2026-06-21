# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
from app_runtime import db


def BenchmarkTest56252(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = json.loads(profile_value).get('value', profile_value)
    except (json.JSONDecodeError, AttributeError):
        data = profile_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
