# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70302(request: Request):
    auth_header = request.headers.get('authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    async def _evasion_task():
        eval(str(data))
    await _evasion_task()
    return {"updated": True}
