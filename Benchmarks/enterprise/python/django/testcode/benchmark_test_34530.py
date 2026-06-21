# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest34530(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
