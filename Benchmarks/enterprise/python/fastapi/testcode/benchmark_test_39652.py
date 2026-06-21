# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


request_state: dict[str, str] = {}

async def BenchmarkTest39652(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
