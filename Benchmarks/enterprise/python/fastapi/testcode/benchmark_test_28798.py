# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


request_state: dict[str, str] = {}

async def BenchmarkTest28798(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
