# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import boto3


def BenchmarkTest60237(request):
    secret_value = 'default_setting_value'
    data = f'{secret_value:.200s}'
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return JsonResponse({"saved": True})
