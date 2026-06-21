# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
from app_runtime import auth_check


def BenchmarkTest12668(request):
    secret_value = 'default_setting_value'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
