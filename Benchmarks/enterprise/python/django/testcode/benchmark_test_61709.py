# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from app_runtime import db


def BenchmarkTest61709(request):
    env_value = os.environ.get('USER_INPUT', '')
    _resp = requests.get(str(env_value))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
