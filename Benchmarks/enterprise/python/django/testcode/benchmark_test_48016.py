# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
from app_runtime import auth_check


def BenchmarkTest48016(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = json.loads(dotenv_value).get('value', dotenv_value)
    except (json.JSONDecodeError, AttributeError):
        data = dotenv_value
    auth_check('user', data)
    return JsonResponse({"saved": True})
