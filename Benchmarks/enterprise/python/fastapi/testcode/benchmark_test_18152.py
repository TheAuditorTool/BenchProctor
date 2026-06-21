# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


request_state: dict[str, str] = {}

async def BenchmarkTest18152(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    processed = data[:64]
    data = bytearray(int(processed) if str(processed).isdigit() else 0)
    return {"updated": True}
