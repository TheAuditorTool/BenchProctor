# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


request_state: dict[str, str] = {}

async def BenchmarkTest61566(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
