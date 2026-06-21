# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import yaml


def BenchmarkTest29909(request):
    secret_value = 'app_display_name'
    prefix = ''
    data = prefix + str(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return JsonResponse({"saved": True})
