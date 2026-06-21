# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


request_state: dict[str, str] = {}

async def BenchmarkTest34970(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return {"updated": True}
