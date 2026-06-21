# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


request_state: dict[str, str] = {}

async def BenchmarkTest47142(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
