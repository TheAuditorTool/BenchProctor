# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


request_state: dict[str, str] = {}

async def BenchmarkTest02136(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
