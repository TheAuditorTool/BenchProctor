# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import requests


request_state: dict[str, str] = {}

async def BenchmarkTest01318(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
