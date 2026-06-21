# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest09660(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
