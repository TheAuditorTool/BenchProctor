# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


request_state: dict[str, str] = {}

async def BenchmarkTest78381(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
