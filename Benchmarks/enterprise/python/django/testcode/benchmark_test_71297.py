# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import yaml


def BenchmarkTest71297(request):
    secret_value = 'default_config_label'
    data = f'{secret_value:.200s}'
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
