# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


request_state: dict[str, str] = {}

async def BenchmarkTest10477(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return {"updated": True}
