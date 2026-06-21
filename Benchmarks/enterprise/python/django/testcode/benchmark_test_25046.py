# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest25046(request):
    secret_value = 'feature_flag_value'
    data = to_text(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
