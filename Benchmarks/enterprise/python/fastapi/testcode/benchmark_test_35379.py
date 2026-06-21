# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


request_state: dict[str, str] = {}

async def BenchmarkTest35379(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    globals()['counter'] = int(data)
    return {"updated": True}
