# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest62142(request):
    secret_value = 'default_config_label'
    data = normalise_input(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
