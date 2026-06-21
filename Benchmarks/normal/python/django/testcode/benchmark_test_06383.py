# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import db


def BenchmarkTest06383(request):
    secret_value = 'app_display_name'
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    db.connect(host='localhost', user=str(secret_value), password=store_cred)
    return JsonResponse({"saved": True})
