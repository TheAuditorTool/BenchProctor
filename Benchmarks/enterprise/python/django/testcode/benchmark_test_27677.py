# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest27677(request):
    secret_value = 'default_setting_value'
    data = default_blank(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
