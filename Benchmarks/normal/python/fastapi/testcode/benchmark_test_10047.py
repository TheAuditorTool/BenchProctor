# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import keyring


async def BenchmarkTest10047(request: Request):
    secret_value = 'app_display_name'
    store_cred = keyring.get_password('app', 'service-account')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(secret_value)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return {"updated": True}
