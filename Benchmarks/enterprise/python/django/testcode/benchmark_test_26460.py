# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import db


def BenchmarkTest26460(request):
    secret_value = 'feature_flag_value'
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return JsonResponse({"saved": True})
