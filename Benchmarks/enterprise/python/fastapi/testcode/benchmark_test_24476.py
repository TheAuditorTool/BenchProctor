# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


request_state: dict[str, str] = {}

async def BenchmarkTest24476(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
