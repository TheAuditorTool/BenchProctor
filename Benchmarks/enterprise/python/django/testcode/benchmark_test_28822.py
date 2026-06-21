# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import yaml


def BenchmarkTest28822(request):
    secret_value = 'app_display_name'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
