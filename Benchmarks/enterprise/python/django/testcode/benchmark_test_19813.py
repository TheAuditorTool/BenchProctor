# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import yaml
import json


def BenchmarkTest19813(request):
    secret_value = 'default_setting_value'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
