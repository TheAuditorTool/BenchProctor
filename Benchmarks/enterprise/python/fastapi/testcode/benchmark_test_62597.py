# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


request_state: dict[str, str] = {}

async def BenchmarkTest62597(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
