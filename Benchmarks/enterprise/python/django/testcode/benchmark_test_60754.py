# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest60754(request):
    secret_value = 'default_setting_value'
    data = relay_value(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return JsonResponse({"saved": True})
