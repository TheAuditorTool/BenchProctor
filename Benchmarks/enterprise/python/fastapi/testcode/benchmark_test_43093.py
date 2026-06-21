# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import boto3


async def BenchmarkTest43093(request: Request):
    secret_value = 'default_setting_value'
    if secret_value:
        data = secret_value
    else:
        data = ''
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return {"updated": True}
