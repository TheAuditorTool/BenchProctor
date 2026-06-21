# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


request_state: dict[str, str] = {}

async def BenchmarkTest46059(request: Request):
    referer_value = request.headers.get('referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    os.remove(str(data))
    return {"updated": True}
