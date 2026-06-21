# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os
import json


def BenchmarkTest45120(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
