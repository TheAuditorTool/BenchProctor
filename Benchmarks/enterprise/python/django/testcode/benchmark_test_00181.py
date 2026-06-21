# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest00181(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(config_value), store_cred)
    return JsonResponse({"saved": True})
