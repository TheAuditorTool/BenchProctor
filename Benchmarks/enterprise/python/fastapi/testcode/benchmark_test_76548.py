# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


request_state: dict[str, str] = {}

async def BenchmarkTest76548(request: Request):
    origin_value = request.headers.get('origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    globals()['counter'] = int(data)
    return {"updated": True}
