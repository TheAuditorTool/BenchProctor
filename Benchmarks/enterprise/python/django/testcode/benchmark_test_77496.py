# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
from app_runtime import db


def BenchmarkTest77496(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
