# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import keyring


def BenchmarkTest41022(request):
    secret_value = 'default_config_label'
    data = secret_value if secret_value else 'default'
    store_cred = keyring.get_password('app', 'service-account')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return JsonResponse({"saved": True})
