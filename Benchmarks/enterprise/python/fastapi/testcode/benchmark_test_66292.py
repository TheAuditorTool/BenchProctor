# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest66292(request: Request):
    secret_value = 'config_secret_test_abc123'
    if secret_value:
        data = secret_value
    else:
        data = ''
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return {"updated": True}
