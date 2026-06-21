# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import yaml


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest40007(request):
    secret_value = 'app_display_name'
    data = default_blank(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
