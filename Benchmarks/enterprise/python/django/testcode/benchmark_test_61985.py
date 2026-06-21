# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest61985(request):
    secret_value = 'default_config_label'
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(secret_value), store_cred)
    return JsonResponse({"saved": True})
