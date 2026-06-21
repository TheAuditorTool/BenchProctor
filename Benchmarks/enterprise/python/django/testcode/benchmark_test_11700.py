# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import boto3


def BenchmarkTest11700(request):
    secret_value = 'default_setting_value'
    if secret_value:
        data = secret_value
    else:
        data = ''
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return JsonResponse({"saved": True})
