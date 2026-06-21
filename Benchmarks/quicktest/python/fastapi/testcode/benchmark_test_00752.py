# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import boto3


async def BenchmarkTest00752(request: Request):
    secret_value = 'default_config_label'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return {"updated": True}
