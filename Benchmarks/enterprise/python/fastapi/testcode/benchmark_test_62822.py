# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


request_state: dict[str, str] = {}

async def BenchmarkTest62822(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    await _evasion_task()
    return {"updated": True}
