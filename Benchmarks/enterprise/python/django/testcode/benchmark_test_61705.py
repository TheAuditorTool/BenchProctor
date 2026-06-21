# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest61705(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    if yaml_value:
        data = yaml_value
    else:
        data = ''
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
