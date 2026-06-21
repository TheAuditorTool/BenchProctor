# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


request_state: dict[str, str] = {}

async def BenchmarkTest47678(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
