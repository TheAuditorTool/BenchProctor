# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest73490(request: Request):
    auth_header = request.headers.get('authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    await _evasion_task()
    return {"updated": True}
