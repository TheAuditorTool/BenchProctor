# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
from app_runtime import db


def BenchmarkTest66380(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JsonResponse({'secret': str(secret)}, status=200)
