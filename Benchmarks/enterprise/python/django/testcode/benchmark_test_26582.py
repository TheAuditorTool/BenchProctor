# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest26582(request):
    secret_value = 'default_config_label'
    data = secret_value if secret_value else 'default'
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
