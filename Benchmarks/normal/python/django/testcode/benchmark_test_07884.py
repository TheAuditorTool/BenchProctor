# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import keyring


def BenchmarkTest07884(request):
    secret_value = 'app_display_name'
    store_cred = keyring.get_password('app', 'service-account')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(secret_value)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return JsonResponse({"saved": True})
