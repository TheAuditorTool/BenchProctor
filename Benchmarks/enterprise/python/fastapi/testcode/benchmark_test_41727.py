# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import boto3


async def BenchmarkTest41727(request: Request):
    secret_value = 'default_setting_value'
    data = (lambda v: v.strip())(secret_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return {"updated": True}
