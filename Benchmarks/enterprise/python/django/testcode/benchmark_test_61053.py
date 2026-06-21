# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest61053(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    if config_value:
        data = config_value
    else:
        data = ''
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
