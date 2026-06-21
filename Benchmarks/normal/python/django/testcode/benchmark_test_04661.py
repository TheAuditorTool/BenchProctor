# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
from app_runtime import db


def BenchmarkTest04661(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
