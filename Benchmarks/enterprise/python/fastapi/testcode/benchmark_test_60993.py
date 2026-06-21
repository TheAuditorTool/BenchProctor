# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


request_state: dict[str, str] = {}

async def BenchmarkTest60993(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    request_state['last_input'] = dotenv_value
    data = request_state['last_input']
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
