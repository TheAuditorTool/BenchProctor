# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from app_runtime import db


def BenchmarkTest44639(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
