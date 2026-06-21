# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest26885(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = default_blank(config_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
