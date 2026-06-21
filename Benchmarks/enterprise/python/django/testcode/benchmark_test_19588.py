# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import json
from app_runtime import db


def BenchmarkTest19588(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
