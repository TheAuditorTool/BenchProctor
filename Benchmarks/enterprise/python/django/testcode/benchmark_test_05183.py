# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest05183(request):
    secret_value = 'default_setting_value'
    data = default_blank(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
