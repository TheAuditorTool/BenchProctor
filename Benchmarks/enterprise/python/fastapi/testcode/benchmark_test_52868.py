# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


request_state: dict[str, str] = {}

async def BenchmarkTest52868(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
